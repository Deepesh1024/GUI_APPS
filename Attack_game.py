import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, 
                             QProgressBar, QHBoxLayout)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QSound

# Player and Enemy classes
class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.health = 100
        self.stamina = 0

class Enemy:
    def __init__(self):
        self.name = "Goblin"
        self.health = 100

# Function to simulate attacks
def attack(attack_type):
    damage = 0
    if attack_type == 1:
        damage = 5
    elif attack_type == 2:
        damage = 10
    elif attack_type == 3:
        damage = 20
    return damage

# Function to generate random attack for the enemy
def get_enemy_attack():
    # The Goblin uses water attacks most, air attacks rarely, and never land attacks
    return random.choices([1, 2], [0.2, 0.8])[0]  # Rarely air (20%), mostly water (80%)

# Game window class
class GameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.player = Player()
        self.enemy = Enemy()

        # Load sound effects
        self.air_attack_sound = QSound("Thrall Claw Attack Sound Effect Third Variation.wav")
        self.water_attack_sound = QSound("Thrall Claw Attack Sound Effect Third Variation.wav")
        self.land_attack_sound = QSound("Thrall Claw Attack Sound Effect Third Variation.wav")

        # Set up the layout
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Background color
        self.setStyleSheet("background-color: black;")

        # Player and enemy health bars
        self.player_health_bar = QProgressBar(self)
        self.player_health_bar.setValue(self.player.health)
        self.player_health_bar.setStyleSheet("QProgressBar::chunk { background-color: #3b7dd8; }")

        self.enemy_health_bar = QProgressBar(self)
        self.enemy_health_bar.setValue(self.enemy.health)
        self.enemy_health_bar.setStyleSheet("QProgressBar::chunk { background-color: #d83b3b; }")

        layout.addWidget(self.player_health_bar)
        layout.addWidget(self.enemy_health_bar)

        # Attack buttons with colors
        self.air_attack_btn = QPushButton("Air Attack (5 Damage)", self)
        self.air_attack_btn.setStyleSheet("""
            QPushButton {
                background-color: #66bb6a; 
                color: white; 
                padding: 10px; 
                font-size: 16px; 
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #43a047;
            }
        """)
        
        self.water_attack_btn = QPushButton("Water Attack (10 Damage)", self)
        self.water_attack_btn.setStyleSheet("""
            QPushButton {
                background-color: #42a5f5; 
                color: white; 
                padding: 10px; 
                font-size: 16px; 
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #1e88e5;
            }
        """)
        
        self.land_attack_btn = QPushButton("Land Attack (20 Damage)", self)
        self.land_attack_btn.setStyleSheet("""
            QPushButton {
                background-color: #ef5350; 
                color: white; 
                padding: 10px; 
                font-size: 16px; 
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #e53935;
            }
        """)

        layout.addWidget(self.air_attack_btn)
        layout.addWidget(self.water_attack_btn)
        layout.addWidget(self.land_attack_btn)

        # Connect buttons to actions
        self.air_attack_btn.clicked.connect(self.perform_air_attack)
        self.water_attack_btn.clicked.connect(self.perform_water_attack)
        self.land_attack_btn.clicked.connect(self.perform_land_attack)

        self.setLayout(layout)
        self.setWindowTitle("Battle Game")
        self.setFixedSize(800, 600)  # Increased window size for better responsiveness

    def perform_air_attack(self):
        # No stamina cost for air attack
        self.air_attack_sound.play()  # Play sound for air attack
        self.attack_enemy(1)
        # Increase stamina after attack
        self.player.stamina += 1

    def perform_water_attack(self):
        if self.player.stamina >= 2:
            self.player.stamina -= 2
            self.water_attack_sound.play()  # Play sound for water attack
            self.attack_enemy(2)
        else:
            QMessageBox.warning(self, "Insufficient Stamina", "Not enough stamina for Water Attack!")

    def perform_land_attack(self):
        if self.player.stamina >= 3:
            self.player.stamina -= 3
            self.land_attack_sound.play()  # Play sound for land attack
            self.attack_enemy(3)
        else:
            QMessageBox.warning(self, "Insufficient Stamina", "Not enough stamina for Land Attack!")

    def attack_enemy(self, attack_type):
        # Player attacks enemy
        self.enemy.health -= attack(attack_type)
        self.enemy_health_bar.setValue(self.enemy.health)

        # Check if the enemy is defeated
        if self.enemy.health <= 0:
            QMessageBox.information(self, "Game Over", "You won!")
            self.reset_game()
            return

        # Enemy attacks player
        enemy_attack_type = get_enemy_attack()
        self.player.health -= attack(enemy_attack_type)
        self.player_health_bar.setValue(self.player.health)

        # Check if the player is defeated
        if self.player.health <= 0:
            QMessageBox.information(self, "Game Over", "You lost!")
            self.reset_game()

    def reset_game(self):
        # Reset the game health values
        self.player.health = 100
        self.enemy.health = 100
        self.player.stamina = 0
        self.player_health_bar.setValue(self.player.health)
        self.enemy_health_bar.setValue(self.enemy.health)

# Main function to run the application
def main():
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
