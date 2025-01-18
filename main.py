def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    report_text = get_report(book_path, num_words, chars_sorted_list)
    print(report_text)


def sort_on(d: dict):
    return d["num"]


def get_report(book_path: str, num_words: str, chars_sorted_list: list[dict[str:int]]):
    report_text = f"--- Begin report of {book_path} ---\n"
    report_text += f"{num_words} words found in the document\n\n"

    for item in chars_sorted_list:
        if not item["name"].isalpha():
            continue
        report_text += f"The '{item['name']}' character was found {item['num']} times\n"
    report_text += "--- End report ---"
    return report_text


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_num_words(text: str):
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> list[dict]:
    chars = {}
    text = text.lower()
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def chars_dict_to_sorted_list(chars_dict: dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"name": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


if __name__ == "__main__":
    main()
