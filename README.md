# Campus Navigation & Utility Planner  
**Data Structures – Assignment 3 (Trees & Graphs)**  
**Course Code:** ENCS205  
**Semester:** 3rd  

This project implements a complete **Campus Navigation and Utility Planner** using core data structures from the syllabus, including **Binary Search Trees, AVL Trees, Graphs, Dijkstra’s Algorithm, Kruskal’s MST**, and **Expression Trees**.

The system models university buildings, stores their information, manages traversal of locations, and computes optimal navigation and utility layouts.

## 🚀 Features Implemented

### ✔ Building Data ADT  
Each building contains:  
- `BuildingID`  
- `BuildingName`  
- `LocationDetails`

===

## 🌳 Part 1 — Tree Implementations

### **1. Binary Search Tree (BST)**
- Insert building record  
- Search by BuildingID  
- Traversals: Inorder, Preorder, Postorder  
- Height calculation  

### **2. AVL Tree**
- Self-balancing tree for efficient lookup  
- Supports rotations: **LL, RR, LR, RL**  
- Automatic height balancing  
- Traversal + height comparison with BST  

---

## 🌐 Part 2 — Graph Implementations

### **CampusGraph**
Buildings are represented as nodes and paths as weighted edges.

Implemented using:
- **Adjacency List**
- **Adjacency Matrix**

### Traversal Algorithms
- **BFS** (Breadth First Search)  
- **DFS** (Depth First Search)  

### Optimal Route Calculation
- **Dijkstra’s Algorithm**  
Finds shortest path from source building.

### Utility Layout Planning
- **Kruskal’s Minimum Spanning Tree (MST)**  
Used for cost-efficient cable/utility connections.

---

## 🔢 Expression Tree (Energy Bill Evaluation)
Implements arithmetic expression trees to compute energy bills using operators:
- `+`, `-`, `*`, `/`

Postfix expressions are converted to an expression tree and evaluated.

---

## 📁 Project Structure

