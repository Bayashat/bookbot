# 📚 BookBot

**BookBot** is a command-line application written in Python that performs static analysis on text files—perfect for analyzing entire novels like *"Frankenstein"*.

> This project is an excellent starting point for Python beginners, brought to you by the [Boot.dev](https://www.boot.dev/tracks/backend) courses.

---

## ✨ Features

- Analyze text files or novels for:
  - Word count
  - Sentence count (if applicable)
  - Character frequency
  - Other useful text statistics
- Easy-to-use command-line interface
- Modular and beginner-friendly code structure

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or above
- Basic familiarity with command-line tools
- A text file or novel to analyze (e.g., *"Frankenstein"*)

### Installation & Running
1.  Clone or download this repository.
2.  Place your `.txt` text file (e.g., `frankenstein.txt`) into the `books/` directory.
3.  Open your terminal and navigate to the project's root directory.
4.  Run the application by providing the path to the book file as a command-line argument:
    ```bash
    python main.py books/your_book_file.txt
    ```
    Replace `books/your_book_file.txt` with the actual path to your book. If you run `python main.py` without specifying a book path, the program will display a usage message and exit.

---

## 🛠️ Usage

To use BookBot, run the `main.py` script from your terminal, followed by the path to the text file you want to analyze.

For example, if you have a file named `frankenstein.txt` in the `books/` directory, you would run:
```bash
python main.py books/frankenstein.txt
```

If you run `python main.py` without specifying a book path, the program will display the following usage message and exit:
```
Usage: python3 main.py <path_to_book>
```

The program will then output:
- The total word count of the book.
- The count of each character's appearance in the book (sorted alphabetically, case-insensitive).

---

## 📖 About Boot.dev

This project is part of the Boot.dev backend track, an online platform for learning backend development with practical, project-based courses.

---

## 🔗 Useful Links
- [Boot.dev Backend Track](https://www.boot.dev/tracks/backend)
- [Frankenstein - Project Gutenberg](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt) (sample text for testing)

---

## 📄 License

This project does not specify a license. Please consider this before distributing or modifying it.

---

## 🎉 Happy coding!