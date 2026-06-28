# Code Cultivation: Object-Oriented Garden Systems

## Module Overview
[cite_start]Welcome to the CodeCultivation ecosystem[cite: 71]. [cite_start]This module serves as a progressive journey into Python 3.10+ fundamentals, transitioning systematically from procedural script structures into advanced Object-Oriented Programming (OOP) architectures[cite: 72, 73, 83, 89]. 

[cite_start]Through the lens of building a data-driven community garden management system, this module explores encapsulation, inheritance, method overrides, nested components, and polymorphism[cite: 3, 72, 76, 193, 206].

---

## Global Requirements & Project Standards

All deliverables throughout this module must strictly adhere to the following baseline development criteria:
* [cite_start]**Runtime Environment**: Python 3.10+[cite: 89].
* [cite_start]**Code Quality**: 100% compliance with `flake8` linter standards[cite: 90].
* [cite_start]**Type Safety**: Full static type-hint annotations checked and verified via `mypy`[cite: 93].
* **Naming Conventions**: `PascalCase` for class definitions; [cite_start]`snake_case` for variables, attributes, and functions[cite: 92].
* [cite_start]**Directory Layout**: Each exercise must reside within its own dedicated directory using the exact naming structure indicated below[cite: 91].

---

## Module Roadmap & Exercises

[cite_start]The codebase builds layer-by-layer, where each sequential exercise expands upon the classes and logic established in the previous step[cite: 12, 81, 101].

### [ex0] Exercise 0: Planting Your First Seed
* [cite_start]**Directory**: `ex0/` [cite: 109]
* [cite_start]**Target File**: `ft_garden_intro.py` [cite: 111]
* [cite_start]**Core Focus**: Execution entry points and basic variable mapping[cite: 113, 120].
* [cite_start]**Description**: Introduces the foundational execution pattern `if __name__ == "__main__":` and standardizes script behavior using localized variables to track plant metadata (name, height, age)[cite: 119, 120].

### [ex1] Exercise 1: Garden Data Organizer
* [cite_start]**Directory**: `ex1/` [cite: 148]
* [cite_start]**Target File**: `ft_garden_data.py` [cite: 150]
* [cite_start]**Core Focus**: Object instantiation and baseline class structures[cite: 159, 161].
* [cite_start]**Description**: Shifts data management from isolated variables into a structured blueprint by creating the initial `Plant` class[cite: 159, 160]. [cite_start]Introduces the standard `show()` method to output formatted instance states[cite: 162].

### [ex2] Exercise 2: Plant Growth Simulator
* [cite_start]**Directory**: `ex2/` [cite: 171]
* [cite_start]**Target File**: `ft_plant_growth.py` [cite: 171]
* [cite_start]**Core Focus**: Instance methods and mutable state modifications[cite: 172].
* [cite_start]**Description**: Models dynamic behaviors over time by implementing `grow()` and `age()` methods directly onto the `Plant` class to alter spatial and temporal data attributes[cite: 173].

### [ex3] Exercise 3: Plant Factory
* [cite_start]**Directory**: `ex3/` [cite: 179]
* [cite_start]**Target File**: `ft_plant_factory.py` [cite: 179]
* [cite_start]**Core Focus**: Constructor orchestration and streamlined instantiation[cite: 180].
* [cite_start]**Description**: Optimizes object lifecycle management using the `__init__` constructor method[cite: 180]. [cite_start]Enables immediate state setup during instantiation for multiple, distinct plant entities[cite: 180, 181].

### [ex4] Exercise 4: Garden Security System
* [cite_start]**Directory**: `ex4/` [cite: 186]
* [cite_start]**Target File**: `ft_garden_security.py` [cite: 186]
* [cite_start]**Core Focus**: Encapsulation and data validation boundaries[cite: 188, 190].
* [cite_start]**Description**: Protects state attributes from corruptive mutations (such as negative age or height markers)[cite: 187, 189]. [cite_start]Enforces Python's "protected" single-underscore naming convention and channels data alterations through explicit getters and setters (`get_height()`, `set_height()`)[cite: 189].

### [ex5] Exercise 5: Specialized Plant Types
* [cite_start]**Directory**: `ex5/` [cite: 192]
* [cite_start]**Target File**: `ft_plant_types.py` [cite: 192]
* [cite_start]**Core Focus**: Inheritance, method overrides, and superclass delegation[cite: 193, 195].
* [cite_start]**Description**: Implements class hierarchies by introducing specialized children derived from `Plant`: `Flower` (handling bloom transitions), `Tree` (canopy properties), and `Vegetable` (scaling nutritional algorithms)[cite: 194]. [cite_start]Leverages `super()` to augment parent behaviors cleanly without code duplication[cite: 194, 195, 199].

### [ex6] Exercise 6: Garden Analytics
* [cite_start]**Directory**: `ex6/` [cite: 205]
* [cite_start]**Target File**: `ft_garden_analytics.py` [cite: 205]
* [cite_start]**Core Focus**: Composition, static/class decorators, deep inheritance, and polymorphism[cite: 206, 213].
* [cite_start]**Description**: The capstone architecture integration[cite: 218]. [cite_start]Adds deep multi-level inheritance via a `Seed` class (extending `Flower`)[cite: 209]. [cite_start]Integrates diagnostics by nesting a private `Stats` tracking engine inside `Plant`[cite: 210]. [cite_start]Features `@classmethod` and `@staticmethod` operational tooling, alongside an decoupled standalone polymorphic function to aggregate analytics for any arbitrary plant type[cite: 207, 208, 212, 213].

---

## Technical Verification Commands

[cite_start]To validate compliance with the general instructions before a project submission defense, execute the following commands from the project root[cite: 93, 223, 224]:

```bash
# 1. Check coding convention formatting across all directories
flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/

# 2. Assert static type declaration contracts pass strict type-checking
mypy ex0/ ex1/ ex2/ ex3/ ex4/ ex5/ ex6/

# 3. Sample execution of the terminal analytic dashboard
python3 ex6/ft_garden_analytics.py