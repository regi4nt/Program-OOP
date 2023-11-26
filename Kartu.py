import json
import random
import subprocess

#Sambutan Pengguna
print('='*80)
print("LOGIKA DAN ALGORITMA PEMROGRAMAN")
print("Selamat Datang di Program OOP dengan Inheritance dan Polimorphism pada Bahasa Python")

# Menunggu pengguna menekan Enter
input('='*80)

# Class Induk / Superclass
class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.attack = random.randint(1, 10)
        self.health = random.randint(1, 10)

    def info(self):
        return f"Player: {self.name}, Class: {self.player_class}, Attack: {self.attack}, Health: {self.health}"

    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} menyerang {enemy.name} dengan serangan {self.attack}!")
        print(f"Health {enemy.name} tersisa: {enemy.health}")
    
    def to_dict(self):
        return {
            "name": self.name,
            "class": self.player_class,
            "attack": self.attack,
            "health": self.health
        }

# Subclass untuk tiap class pemain
class Guardian(Player):
    def __init__(self, name):
        super().__init__(name, 'Guardian')
        self.attack = 8
        self.health = 120

    def special_ability(self):
        return f"{self.name} memiliki kemampuan pelindung yang kuat!"

class Caster(Player):
    def __init__(self, name):
        super().__init__(name, 'Caster')
        self.attack = 15
        self.health = 80

    def special_ability(self):
        return f"{self.name} memiliki kekuatan sihir yang luar biasa!"

class Fighter(Player):
    def __init__(self, name):
        super().__init__(name, 'Fighter')
        self.attack = 12
        self.health = 100

    def special_ability(self):
        return f"{self.name} ahli dalam pertarungan jarak dekat!"

class Archer(Player):
    def __init__(self, name):
        super().__init__(name, 'Archer')
        self.attack = 14
        self.health = 90

    def special_ability(self):
        return f"{self.name} sangat mahir dalam memanah target!"

class Supporter(Player):
    def __init__(self, name):
        super().__init__(name, 'Supporter')
        self.attack = 5
        self.health = 110

    def special_ability(self):
        return f"{self.name} mampu memberikan bantuan kepada rekan satu tim!"

# Class Monster
class Monster:
    def __init__(self, name):
        self.name = name
        self.attack = random.randint(8, 15)
        self.health = random.randint(80, 120)

    def info(self):
        return f"Monster: {self.name}, Attack: {self.attack}, Health: {self.health}"

    def attack_player(self, player):
        player.health -= self.attack
        print(f"{self.name} menyerang {player.name} dengan serangan {self.attack}!")
        print(f"Health {player.name} tersisa: {player.health}")

class Game:
    @staticmethod
    def save_to_json(players):
        players_data = {"players": [player.to_dict() for player in players]}
        with open("players.json", "w") as file:
            json.dump(players_data, file, indent=4)
        print("Player data saved to players.json")

    @staticmethod
    def fight(player1, player2):
        if player1.attack > player2.health:
            print(f"{player1.name} wins!")
        elif player2.attack > player1.health:
            print(f"{player2.name} wins!")
        else:
            print("It's a draw!")

# Fungsi untuk membuat akun player dengan class acak
def create_player_account(player_name):
    player_classes = [Guardian, Caster, Fighter, Archer, Supporter]
    chosen_class = random.choice(player_classes)
    return chosen_class(player_name)

#Informasi Angka
while True:
    print("Selamat datang! Silakan pilih opsi:")
    print("1. Singleplayer")
    print("2. Multiplayer")
    print("3. History")
    print("4. Quit")

    choice = input("Masukkan nomor opsi: ")
    if choice == "1":
        print()

        # Contoh penggunaan:
        player_name = input("Masukkan nama player: ")
        new_player = create_player_account(player_name)
        print("Akun player berhasil dibuat!")
        print(new_player.info())
        print()

        # Membuat monster secara acak
        monsters = ["Goblin", "Troll", "Orc", "Dragon"]
        random_monster = Monster(random.choice(monsters))
        print(f"Muncul sebuah monster: {random_monster.name}")
        print(random_monster.info())
        print()

        # Pertarungan antara player dan monster
        while new_player.health > 0 and random_monster.health > 0:
            # Giliran player menyerang monster
            new_player.attack_enemy(random_monster)
            if random_monster.health <= 0:
                print(f"{random_monster.name} dikalahkan!")
                break

            # Giliran monster menyerang player
            random_monster.attack_player(new_player)
            if new_player.health <= 0:
                print(f"{new_player.name} kalah dalam pertarungan.")
                break

        # Menampilkan hasil akhir pertarungan
        print("\nHasil akhir pertarungan:")
        print(new_player.info())
        print(random_monster.info())
        input()

    elif choice == "2":
        # Player account creation
        def create_player():
            print()
            player_name = input("Enter player name: ")
            new_player = create_player_account(player_name)
            print(new_player.info())
            return new_player

        # Creating players
        players = []
        for _ in range(2):
            player = create_player()
            players.append(player)

        # Saving player data to JSON
        print()
        Game.save_to_json(players)

        # Simulating a fight between players
        print("\nSimulating a fight:")
        Game.fight(players[0], players[1])
        input()
 
    elif choice == "3":

        # Fungsi untuk membaca data dari file JSON
        def read_and_display_player_data(file_name):
            try:
                with open(file_name, 'r') as file:
                    data = json.load(file)
                    players = data["players"]

                    print("Data Pemain yang Tersimpan:")
                    for player in players:
                        print(f"Nama: {player['name']}")
                        print(f"Health: {player['health']}")
                        print(f"Attack: {player['attack']}")
                        input()
            except FileNotFoundError:
                print("File tidak ditemukan. Pastikan nama file benar.")
            except json.JSONDecodeError as e:
                print(f"Error dalam membaca file JSON: {e}")

        # Nama file JSON yang akan dibaca
        file_name = 'players.json'

        # Menampilkan kembali data pemain yang telah disimpan
        print()
        read_and_display_player_data(file_name)

    elif choice == "4":
        break

    else:
        print("Opsi tidak valid. Silakan pilih lagi.")

#Penutup
input('='*80)
print("Terima kasih! Program selesai.")
print()
subprocess.run(["python", "Aplikasi.py"])
