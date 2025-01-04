from flask import Flask, jsonify, request
from flask_cors import CORS
from rdkit import Chem
from rdkit.Chem import AllChem
from urllib.error import URLError
from urllib.request import urlopen
from rdkit import Geometry
import math
import requests
import wolframalpha

app_id = "LTXQW8-5ALR8X82XY"
client = wolframalpha.Client(app_id)


app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


@app.route('/generate_sdf', methods=['POST'])
def generate_sdf():
    # Get common name from the request's JSON body
    name = request.json.get('smiles').lower()
    try:
        url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + name.replace(' ', '%20') + '/cids/txt'
        smilesurl = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/' + name.replace(' ', '%20') + '/property/CanonicalSMILES/txt'
        res = client.query(f"{name} lewis structure")      
        answer = next(res.results)
        lewisurl = answer["subpod"]["img"]["@src"]
        response = requests.get(url)
        response2 = requests.get(smilesurl)
        smiles = response2.text.strip()
        cid = response.text.strip()

    except URLError:
        return jsonify({'error': 'Unable to reach the conversion service or invalid name'}), 400

    try:
        mol = Chem.MolFromSmiles(smiles)
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol)
        url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/' + cid +'/record/SDF?record_type=3d&response_type=display'
        if (requests.get(url).status_code == 404):
            sdf_representation = Chem.MolToMolBlock(mol)
        else:
            sdf_representation = urlopen(url).read().decode('utf8')
        hybridization = []
        for atom in mol.GetAtoms():
            hybridization.append(atom.GetHybridization().name)

    except:
        return jsonify({'error': 'Unable to generate molecule from SMILES string'}), 400

    return jsonify({'sdf': sdf_representation, 'url': lewisurl, 'hybridization': hybridization})



if __name__ == '__main__':
    app.run(port=5010)
