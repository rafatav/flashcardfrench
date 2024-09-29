from tkinter import Tk, Canvas, Button, PhotoImage
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
removed_word = {}


# ----------------------------- GENERATE WORD -----------------------------------#

def right_clicked():
    try:
        pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data.to_csv("data/words_to_learn.csv", index=False, encoding="utf-8")
    finally:
        data_learn = pandas.read_csv("data/words_to_learn.csv")
        languages_dict_learn = data_learn.to_dict(orient="records")
        if len(languages_dict_learn) == 0:
            pass
        else:
            languages_dict_learn.remove(removed_word)
            data_learn = pandas.DataFrame(languages_dict_learn)
            data_learn.to_csv("./data/words_to_learn.csv", index=False, encoding="utf-8")
            languages_dict = languages_dict_learn
    generate_word()


def generate_word():
    global current_card, add_timer, removed_word
    random_word = random.choice(languages_dict)
    removed_word = random_word
    window.after_cancel(add_timer)

    language_1, language_2 = [language for language, word in random_word.items()]
    word_language_1, word_language_2 = [word for language, word in random_word.items()]

    current_card = {language_2: word_language_2}

    card_front.itemconfig(card_img, image=card_front_img)
    card_front.itemconfig(card_title, text=language_1, fill="black")
    card_front.itemconfig(card_word, text=word_language_1, fill="black")
    add_timer = window.after(3000, update_word)


def update_word():
    card_front.itemconfig(card_title, text="English", fill="white")
    card_front.itemconfig(card_word, text=current_card["English"], fill="white")
    card_front.itemconfig(card_img, image=card_back_img)
    window.after_cancel("show_card")


# ---------------------------------- DATA ---------------------------------------#
try:
    pandas.read_csv("data/words_to_learn.csv")
    data_learn = pandas.read_csv("data/words_to_learn.csv")
    languages_dict = data_learn.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    languages_dict = data.to_dict(orient='records')

# ---------------------------------- GUI ----------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
add_timer = window.after(3000, update_word)

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = card_front.create_image(400, 263, image=card_front_img)
card_title = card_front.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = card_front.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
card_front.grid(column=0, row=0, columnspan=2)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR,
                      command=generate_word)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR,
                      command=right_clicked)
right_button.grid(column=1, row=1)

generate_word()

window.mainloop()
