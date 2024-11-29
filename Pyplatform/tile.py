import pygame  # Thư viện chính để phát triển trò chơi

# Lớp Tile: Đại diện cho một ô gạch hoặc nền tảng trong trò chơi
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()  # Kế thừa từ lớp Sprite của Pygame

        # Đường dẫn đến ảnh đại diện cho ô gạch
        img_path = 'assets/terrain/stone.jpg'

        # Tải ảnh từ đường dẫn
        self.image = pygame.image.load(img_path)

        # Chuyển đổi kích thước ảnh để phù hợp với kích thước ô (size x size)
        self.image = pygame.transform.scale(self.image, (size, size))

        # Lấy hình chữ nhật đại diện cho vị trí và kích thước của ô
        self.rect = self.image.get_rect(topleft=pos)  # Đặt vị trí ban đầu dựa trên `pos`

    # Phương thức update: Cập nhật vị trí ô gạch khi màn hình cuộn (world scroll)
    def update(self, x_shift):
        self.rect.x += x_shift  # Dịch chuyển ô theo trục x với giá trị `x_shift`
