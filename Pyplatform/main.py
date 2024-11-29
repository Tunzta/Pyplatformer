import pygame, sys
from settings import *  # Import các thiết lập cơ bản như WIDTH, HEIGHT
from world import World  # Import lớp World để quản lý thế giới trong trò chơi

pygame.init()

# Tạo màn hình chính với kích thước cố định
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")  # Đặt tiêu đề cho cửa sổ trò chơi


# Định nghĩa lớp Platformer, đại diện cho trò chơi
class Platformer:
    def __init__(self, screen, width, height):
        self.screen = screen  # Màn hình trò chơi
        self.clock = pygame.time.Clock()  # Đồng hồ để kiểm soát tốc độ khung hình
        self.player_event = False  # Biến để theo dõi sự kiện của người chơi (di chuyển, nhảy)

        # Tải và điều chỉnh kích thước hình nền
        self.bg_img = pygame.image.load('assets/terrain/bg.jpg')
        self.bg_img = pygame.transform.scale(self.bg_img, (width, height))

    # Hàm chính chạy vòng lặp trò chơi
    def main(self):
        # Khởi tạo thế giới trò chơi dựa trên bản đồ (world_map)
        world = World(world_map, self.screen)

        # Vòng lặp chính của trò chơi
        while True:
            # Vẽ hình nền lên màn hình
            self.screen.blit(self.bg_img, (0, 0))

            # Xử lý các sự kiện từ người dùng
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Nếu người chơi đóng cửa sổ
                    pygame.quit()
                    sys.exit()


                elif event.type == pygame.KEYDOWN:  # Khi người chơi nhấn phím

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # Nhấn phím mũi tên trái hoặc phím A

                        self.player_event = "left"

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # Nhấn phím mũi tên phải hoặc phím D

                        self.player_event = "right"

                    if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE:  # Nhấn phím mũi tên lên, phím W hoặc phím SPACE (nhảy)

                        self.player_event = "space"

                elif event.type == pygame.KEYUP:  # Khi người chơi nhả phím
                    self.player_event = False  # Không có hành động nào

            # Cập nhật thế giới dựa trên sự kiện người chơi
            world.update(self.player_event)

            # Cập nhật màn hình và điều chỉnh tốc độ khung hình
            pygame.display.update()
            self.clock.tick(60)  # Giới hạn khung hình ở mức 60 FPS


# Điểm bắt đầu của trò chơi
if __name__ == "__main__":
    play = Platformer(screen, WIDTH, HEIGHT)  # Tạo đối tượng trò chơi
    play.main()  # Chạy trò chơi
