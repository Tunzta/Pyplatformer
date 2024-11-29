import pygame

# Định nghĩa lớp Goal để tạo đối tượng mục tiêu trong trò chơi
class Goal(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()  # Kế thừa từ lớp Sprite của Pygame
        img_path = 'assets/goal/gate.png'  # Đường dẫn đến hình ảnh mục tiêu
        self.image = pygame.image.load(img_path)  # Tải hình ảnh mục tiêu
        self.image = pygame.transform.scale(self.image, (size, size))  # Thay đổi kích thước hình ảnh theo tham số 'size'
        self.rect = self.image.get_rect(topleft=pos)  # Định nghĩa vị trí và khung (rect) của mục tiêu

    # Hàm cập nhật vị trí của mục tiêu khi thế giới di chuyển (scroll)
    def update(self, x_shift):
        self.rect.x += x_shift  # Điều chỉnh tọa độ x của mục tiêu dựa trên x_shift (dịch chuyển ngang)
