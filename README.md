# 🏆 LeetCode Challenge

Welcome to my **daily LeetCode challenge** repository! 🚀  
This repo is a personal journey of solving algorithmic problems every day, sharpening problem-solving skills, and building strong coding habits.

---

## 📌 Goals
- Solve at least **one problem per day** on [LeetCode](https://leetcode.com/).
- Improve **algorithmic thinking** and **data structure mastery**.
- Build **consistency and discipline** in problem-solving.
- Document solutions with **clean code** and **clear explanations**.

---

## 📂 Repository Structure
```

leetcode-challenge/
│
├── solutions/
│   ├── 1_two-sum.py
│   ├── 2_add_two_numbers.py
│   ├── 3_longest-substring-without-repeating-characters.py
│   └── ...
│
├── new.sh
└── README.md

```

- All solutions are stored inside the **`solutions/`** folder.  
- File naming convention:  
    `<problem-number>_<problem-name>.py`  
    Example: `1_two-sum.py`  

---

## 🛠️ Tech Stack
- **Language:** Python (main), may include Java/C++ for practice.  
- **Platform:** [LeetCode](https://leetcode.com/)  

---

## 🚀 Usage: Add a New Problem

You can quickly generate a new solution file using the helper script **`new.sh`**.

### Run Command
```bash
bash new.sh "<problem-number>. <problem-title>"
````

or (if the script has execute permission):

```bash
./new.sh "<problem-number>. <problem-title>"
```

> ⚠️ If you see this error: `bash: ./new.sh: Permission denied`
> Run the following command once to grant execute permission:
>
> ```bash
> chmod +x new.sh
> ```

### Examples

```bash
./new.sh "1. Two Sum"
./new.sh "2. Add Two Numbers"
./new.sh "3. Longest Substring Without Repeating Characters"
```


---

## ✅ Progress Tracker
* [ ] 2025-08-21 | [1. Two Sum](solutions/1_two-sum.py)

---

## 📖 Notes

Each solution file may include:

* **Code implementation**
* **Approach explanation (in comments)**
* **Time & space complexity analysis**

---

## 📜 License

This repository is licensed under the [MIT License](./LICENSE).
Feel free to explore, learn, and share! 🙌
