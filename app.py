import random

def mastermind_pro():
    # Αντιστοίχιση αριθμών με χρώματα
    colors_map = {1: 'Κόκκινο', 2: 'Μπλε', 3: 'Πράσινο', 4: 'Κίτρινο', 5: 'Μαύρο', 6: 'Άσπρο'}
    
    print("Διαθέσιμες επιλογές:")
    for num, color in colors_map.items():
        print(f"{num}: {color}")

    # 1. Εισαγωγή Κώδικα με Έλεγχο Εγκυρότητας (Range Check)
    secret_code = []
    print("\n--- Ορισμός Κρυφού Κώδικα από τον Χρήστη ---")
    
    for i in range(5):
        while True:
            try:
                val = int(input(f"Επιλέξτε αριθμό για τη θέση {i+1} (1-6): "))
                if 1 <= val <= 6:
                    secret_code.append(val)
                    break
                else:
                    print("⚠️ Λάθος! Ο αριθμός πρέπει να είναι από 1 έως 6.")
            except ValueError:
                print("⚠️ Άκυρη είσοδος! Παρακαλώ δώστε μόνο αριθμούς.")

    past_guesses = []
    max_attempts = 10
    attempts = 0
    found = False

    # 2. Κύριο Loop Υπολογιστή
    while attempts < max_attempts and not found:
        attempts += 1
        
        # Εύρεση μοναδικής μαντεψιάς από τον υπολογιστή
        while True:
            current_guess = [random.randint(1, 6) for _ in range(5)]
            if current_guess not in past_guesses:
                break
        
        past_guesses.append(current_guess)
        
        # 3. Σύγκριση και Feedback
        correct_position = 0 # Πρώην Black Pegs
        correct_color_only = 0 # Πρώην White Pegs
        
        temp_secret = list(secret_code)
        temp_guess = list(current_guess)

        # Έλεγχος για Σωστή Θέση
        for i in range(4, -1, -1):
            if temp_guess[i] == temp_secret[i]:
                correct_position += 1
                temp_secret.pop(i)
                temp_guess.pop(i)

        # Έλεγχος για Σωστό Χρώμα (σε λάθος θέση)
        for val in temp_guess:
            if val in temp_secret:
                correct_color_only += 1
                temp_secret.remove(val)

        # Μετάφραση για εμφάνιση
        guess_translated = [colors_map[n] for n in current_guess]
        
        print(f"\nΠροσπάθεια {attempts}: {guess_translated}")
        print(f"Αποτελέσματα: Σωστή Θέση: {correct_position} | Σωστό Χρώμα: {correct_color_only}")

        if correct_position == 5:
            found = True
            print("\n🏁 Ο υπολογιστής βρήκε τον κώδικα και κέρδισε!")

    if not found:
        print(f"\n🏆 Συγχαρητήρια! Ο υπολογιστής απέτυχε μετά από {max_attempts} προσπάθειες.")

if __name__ == "__main__":
    mastermind_pro()