---
marp: true
theme: gaia
class: invert

---
 <style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

<br></br><br></br>

# Molecule Visualization Web-App

Bryan Chung

---
# 1. Objective
- To create an interactive web-app where users can easily visualize any chemistry compound in 3 dimensions

**A web-app differs from a traditional website in that it is more interactive and there is no reloading involved--it essentially behaves like a application, but accessble without downloading. It is simply "better" (but much harder to make).

---

# 2. My Approach
- React JavaScript front-end
    - 3D Implementation using WebGL/Three.js
- Python Backend
    - RDKit API
    - PUBChem API
    - WolframAlpha API

---

# 3. A bit of how the 3D render works

1. When a user enters a molecule, I use the PUBChem API to convert the name into a 'CID' (a unique molecule identifier for PUBChem)

2. The CID of the molecule is once again put through PUBChem API to obtain the 'SDF file'. 

3. The frontend code parses the SDF file, which contains relevant information

---


# 4. Challenges
- 3D rendering is very complicated
- Visualizing the dipoles in 3-dimensional space
- Finding a way to load the lewis structure of a molecule
- Debugging

---

# 5. Known Issues/Room for Improvement

- 2-dimensional molecules like Table Salt do not work well
- Some inconsistency in the side description bar
- Dipole positioning issues
- Double-loading issues
- No support for smaller screen sizes < MBP '13 
- Minor issues in safari

---

# 6. Future Plans
- Fix aforementioned issues
- Allow native support for 2-d molecules
- Re-design
- Host on an actual domain (if Loomis wants to pay $2 per month)

___ 
 <style>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

<br></br><br></br>
# 7. Try it out!
# Go to bit.ly/b3clchem

