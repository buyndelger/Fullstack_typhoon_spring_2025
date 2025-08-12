import random

def play_game():
    print("\nТоо таах тоглоом эхэллээ! 🎮")

    # --- Хэцүү байдлын түвшин сонгох ---
    while True:
        difficulty = input("Хэцүү байдлын түвшнийг сонгоно уу ('hylbar', 'дунд', 'хэцүү'): ").lower()
        if difficulty == "hylbar":
            range_end = 50
            attempts = None  
            break
    
    number_to_guess = random.randint(1, range_end)
    print(f"\nБи 1-ээс {range_end} хүртэл нэг тоо бодсон. Та таагаарай!")

    guess_count = 0

    
    while True:
        
        if attempts is not None and attempts - guess_count <= 0:
            print("\n Таны таах боломж дууслаа. Та ялагдлаа. ")
            print(f" Зөв тоо нь {number_to_guess} байсан.")
            break

        if attempts is not None:
            print(f"Үлдсэн боломж: {attempts - guess_count}")

        try:
            guess = int(input("Таамагласан тоо: "))
        except ValueError:
            print(" Тоо оруулна уу.")
            continue

        guess_count += 1

        if guess < number_to_guess:
            print(" Хэт бага байна.")
        elif guess > number_to_guess:
            print(" Хэт өндөр байна.")
        else:
            print(f" Зөв таалаа! Та {guess_count} оролдлогоор таалаа.")
            break

print("Тоо таах тоглоомд тавтай морил! 🎯")
while True:
    play_game()
    again = input("\nДахин тоглох уу? (tiim/ugui): ").lower()
    if again != "tiim":
        print("Тоглосонд баярлалаа. Баяртай! ")
        print("-" * 30)
        break
