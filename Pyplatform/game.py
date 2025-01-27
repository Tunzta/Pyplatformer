import pygame
from settings import HEIGHT, WIDTH

pygame.font.init()

# Định nghĩa lớp Game để quản lý logic trò chơi
class Game:
    def __init__(self, screen):
        # Khởi tạo đối tượng Game
        self.screen = screen  # Màn hình game
        self.font = pygame.font.SysFont("impact", 70)  # Font chữ sử dụng cho thông báo
        self.message_color = pygame.Color("darkorange")  # Màu chữ cho thông báo

    # Hàm xử lý khi người chơi thua (hết mạng hoặc rơi khỏi màn chơi)
    def _game_lose(self, player):
        player.game_over = True  # Cập nhật trạng thái game kết thúc
        small_font = pygame.font.Font(None, 24)
        message = self.font.render('You Lose...', True, self.message_color)  # Tạo thông điệp "Thua cuộc"
        score_msg = self.font.render(f"Your Score: {player.score}", True, self.message_color)
        reset_msg = small_font.render("Press Enter To Play Again", True, pygame.Color("black"))
        self.screen.blit(message, (WIDTH // 3 + 70, 70))  # Hiển thị thông báo trên màn hình
        self.screen.blit(score_msg, (WIDTH // 3, 70 + 120))
        self.screen.blit(reset_msg, (WIDTH // 3, 70 + 240))

    # Hàm xử lý khi người chơi thắng (đạt mục tiêu)
    def _game_win(self, player):
        player.game_over = True  # Cập nhật trạng thái game kết thúc
        player.win = True  # Đánh dấu người chơi đã thắng
        small_font = pygame.font.Font(None, 24)
        message = self.font.render('You Win!!', True, self.message_color)  # Tạo thông điệp "Thắng cuộc"
        score_msg = self.font.render(f"Your Score: {player.score}", True, self.message_color)
        reset_msg = small_font.render("Press Enter To Play Again", True, pygame.Color("black"))
        self.screen.blit(message, (WIDTH // 3, 70))  # Hiển thị thông báo trên màn hình
        self.screen.blit(score_msg,(WIDTH // 3, 70 + 120))
        self.screen.blit(reset_msg, (WIDTH // 3, 70 + 240))

    # Hàm kiểm tra trạng thái game: Thua, thắng hoặc tiếp tục
    def game_state(self, player, goal):
        if player.life <= 0 or player.rect.y >= HEIGHT:  # Hết mạng hoặc rơi khỏi màn chơi
            self._game_lose(player)
        elif player.rect.colliderect(goal.rect):  # Người chơi chạm vào mục tiêu
            self._game_win(player)
        else:
            None  # Không có hành động nào (game tiếp tục)

    # Hàm hiển thị số mạng còn lại của người chơi
    def show_life(self, player):
        life_size = 30  # Kích thước biểu tượng mạng sống
        img_path = "assets/life/life.png"  # Đường dẫn đến ảnh mạng sống
        life_image = pygame.image.load(img_path)  # Tải ảnh mạng sống
        life_image = pygame.transform.scale(life_image, (life_size, life_size))  # Thay đổi kích thước ảnh
        indent = 0  # Khoảng cách giữa các biểu tượng mạng sống
        for life in range(player.life):  # Lặp qua số mạng còn lại
            indent += life_size  # Tăng khoảng cách cho mỗi mạng sống
            self.screen.blit(life_image, (indent, life_size))  # Hiển thị ảnh mạng sống lên màn hình

    def show_score(self, player):
        font = pygame.font.SysFont('impact', 25)
        score_text = font.render(f'Score: {player.score}', True, (0, 0, 0))
        self.screen.blit(score_text, (10, 60))
