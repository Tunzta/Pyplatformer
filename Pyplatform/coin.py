import pygame
from support import import_sprite

# Lớp Coin: Đại diện cho một đồng xu (coin)
class Coin(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.coin_img = import_sprite("assets/coin")  # Danh sách khung hình hoạt ảnh
        self.frame_index = 0  # Chỉ số khung hình hiện tại
        self.animation_speed = 0.15  # Tốc độ chuyển khung hình
        self.size = size  # Kích thước đồng xu

        self.image = self.coin_img[self.frame_index]
        self.image = pygame.transform.scale(self.image, (26, 26))
        self.rect = self.image.get_rect(topleft=position)
        self.mask = pygame.mask.from_surface(self.image)

    def animate(self):
        self.frame_index += self.animation_speed  # Tăng chỉ số khung hình
        if self.frame_index >= len(self.coin_img):  # Nếu vượt quá số khung hình, quay lại khung đầu tiên
            self.frame_index = 0

        # Cập nhật hình ảnh của đồng xu
        self.image = self.coin_img[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (26, 26))
        self.mask = pygame.mask.from_surface(self.image)  # Cập nhật lại mask cho hình ảnh mới

    def update(self, world_shift):
        self.rect.x += world_shift  # Di chuyển theo thế giới
        self.animate()  # Gọi phương thức animate để cập nhật khung hình
