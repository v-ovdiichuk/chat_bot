import random
import time
import sys


try:
    import pyjokes
    import emoji
    from art import tprint
    from colorama import Fore, Style, init
    from tqdm import tqdm  
except ImportError as e:
    print(f"Помилка: Не встановлено необхідну бібліотеку: {e.name}")
    print("Спробуйте: pip install pyjokes art colorama emoji tqdm")
    sys.exit(1)

init(autoreset=True)

# --- ДАНІ ---
DATA_MOVIES = {
    "Бойовик": ["John Wick", "Mad Max: Fury Road", "Die Hard", "The Matrix"],
    "Комедія": ["The Hangover", "Superbad", "Mask", "Home Alone"],
    "Драма": ["The Shawshank Redemption", "Forrest Gump", "The Green Mile"],
    "Фантастика": ["Inception", "Interstellar", "Dune", "Blade Runner 2049"]
}

DATA_MUSIC = {
    "Рок": ["AC/DC - Back in Black", "Nirvana - Smells Like Teen Spirit", "Queen - Bohemian Rhapsody"],
    "Поп": ["Michael Jackson - Billie Jean", "The Weeknd - Blinding Lights", "Dua Lipa - Levitating"],
    "Джаз": ["Louis Armstrong - What a Wonderful World", "Miles Davis - So What", "Frank Sinatra - Fly Me To The Moon"]
}

DATA_GAMES = {
    "RPG": ["The Witcher 3", "Skyrim", "Cyberpunk 2077", "Elden Ring"],
    "Шутер": ["CS:GO", "Call of Duty", "Doom Eternal", "Overwatch 2"],
    "Стратегія": ["Civilization VI", "StarCraft II", "Age of Empires IV"]
}



def simulate_processing(desc="Завантаження", seconds=1):
    """Створює штучний прогрес-бар за допомогою tqdm."""
    # Розбиваємо час на 10 кроків
    chunk = seconds / 10
    for _ in tqdm(range(10), desc=desc, ncols=75, colour='green', bar_format='{l_bar}{bar}|'):
        time.sleep(chunk)
    print() # Порожній рядок після бару

def print_header():
    print(Fore.CYAN)
    tprint("FunBot_3000")
    print(Style.RESET_ALL)
    msg = emoji.emojize(":robot: Привіт! Я твій персональний розважальний асистент.")
    print(Fore.YELLOW + msg)
    print("-" * 50)

def get_category_choice(data_dict, topic_name):
    print(f"\n{Fore.GREEN}Обери жанр для {topic_name}:{Style.RESET_ALL}")
    categories = list(data_dict.keys())
    
    for i, genre in enumerate(categories, 1):
        print(f"{i}. {genre}")
    
    try:
        choice = int(input(f"\n{Fore.CYAN}Твій вибір (номер): {Style.RESET_ALL}"))
        if 1 <= choice <= len(categories):
            # Запуск анімації пошуку
            simulate_processing(desc="Шукаю найкращий варіант", seconds=1)
            
            selected_genre = categories[choice - 1]
            recommendation = random.choice(data_dict[selected_genre])
            return selected_genre, recommendation
        else:
            print(Fore.RED + "Невірний номер категорії.")
            return None, None
    except ValueError:
        print(Fore.RED + "Будь ласка, введіть число.")
        return None, None

# --- ОСНОВНІ ФУНКЦІЇ ---

def feature_movies():
    genre, movie = get_category_choice(DATA_MOVIES, "фільмів")
    if movie:
        icon = emoji.emojize(":clapper_board:")
        print(f"{icon} Рекомендую подивитися у жанрі {genre}: {Fore.MAGENTA}{Style.BRIGHT}{movie}")

def feature_music():
    genre, song = get_category_choice(DATA_MUSIC, "музики")
    if song:
        icon = emoji.emojize(":musical_note:")
        print(f"{icon} Рекомендую послухати ({genre}): {Fore.MAGENTA}{Style.BRIGHT}{song}")

def feature_games_recommendation():
    genre, game = get_category_choice(DATA_GAMES, "ігор")
    if game:
        icon = emoji.emojize(":video_game:")
        print(f"{icon} Спробуй пограти в ({genre}): {Fore.MAGENTA}{Style.BRIGHT}{game}")

def feature_joke():
    print(Fore.YELLOW + "\nПідключаюся до бази гумору..." + Style.RESET_ALL)
    simulate_processing(desc="Завантаження жарту", seconds=1)
    
    joke = pyjokes.get_joke(language='en', category='neutral')
    icon = emoji.emojize(":rolling_on_the_floor_laughing:")
    print(f"{icon} {Fore.CYAN}{joke}")

def game_guess_number():
    title_icon = emoji.emojize(":game_die:")
    print(Fore.GREEN + f"\n=== {title_icon} ГРА: ВГАДАЙ ЧИСЛО ===")
    print("Я загадав число від 1 до 20. У тебе є 5 спроб.")
    
    secret_number = random.randint(1, 20)
    
    for i in range(5):
        try:
            guess = int(input(f"Спроба {i+1}: Введи число: "))
            if guess < secret_number:
                print(Fore.BLUE + "Більше! " + emoji.emojize(":up_arrow:"))
            elif guess > secret_number:
                print(Fore.BLUE + "Менше! " + emoji.emojize(":down_arrow:"))
            else:
                win_icon = emoji.emojize(":party_popper:")
                print(Fore.GREEN + f"{win_icon} Вітаю! Ти вгадав число {secret_number}!")
                return
        except ValueError:
            print(Fore.RED + "Вводь лише цифри!")

    skull = emoji.emojize(":skull:")
    print(Fore.RED + f"{skull} Ти програв. Загадане число було: {secret_number}")

# --- МЕНЮ ---

def show_menu():
    print("\n" + "="*30)
    print(f"{Fore.YELLOW}ГОЛОВНЕ МЕНЮ:{Style.RESET_ALL}")
    print(emoji.emojize("1. :clapper_board: Порадити фільм"))
    print(emoji.emojize("2. :musical_note: Порадити музику"))
    print(emoji.emojize("3. :video_game: Порадити гру"))
    print(emoji.emojize("4. :grinning_face_with_sweat: Розповісти жарт (Англ)"))
    print(emoji.emojize("5. :game_die: Пограти в 'Вгадай число'"))
    print(emoji.emojize("0. :door: Вихід"))
    print("="*30)

def main():
    print_header()
    while True:
        show_menu()
        choice = input(f"{Fore.CYAN}Обери опцію: {Style.RESET_ALL}")
        if choice == "1": feature_movies()
        elif choice == "2": feature_music()
        elif choice == "3": feature_games_recommendation()
        elif choice == "4": feature_joke()
        elif choice == "5": game_guess_number()
        elif choice == "0":
            print(Fore.MAGENTA + emoji.emojize("До зустрічі! :waving_hand:"))
            break
        else:
            print(Fore.RED + "Невідома команда.")
        time.sleep(0.5)

if __name__ == "__main__":
    main()