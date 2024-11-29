import pygame  # Thư viện chính để phát triển trò chơi
from support import import_sprite  # Hàm hỗ trợ để tải các sprite từ thư mục

# Lớp Trap: Đại diện cho một bẫy (trap), cụ thể là bẫy lưỡi dao xoay
class Trap(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()  # Kế thừa từ lớp Sprite của Pygame

        # Tải danh sách các sprite (ảnh) cho hoạt ảnh xoay của lưỡi dao
        self.blade_img = import_sprite("assets/trap")

        # Chỉ số khung hiện tại trong hoạt ảnh
        self.frame_index = 0

        # Độ trễ giữa các khung hình trong hoạt ảnh (càng cao, tốc độ xoay càng chậm)
        self.animation_delay = 3

        # Ảnh hiện tại của bẫy
        self.image = self.blade_img[self.frame_index]

        # Chuyển đổi kích thước ảnh để phù hợp với `size x size`
        self.image = pygame.transform.scale(self.image, (size, size))

        # Tạo mask để kiểm tra va chạm chính xác hơn (không chỉ dựa vào hình chữ nhật)
        self.mask = pygame.mask.from_surface(self.image)

        # Hình chữ nhật bao quanh lưỡi dao, dùng để xác định vị trí và kích thước
        self.rect = self.image.get_rect(topleft=pos)  # Đặt vị trí bẫy tại `pos`

    # Phương thức _animate: Thêm hiệu ứng xoay cho lưỡi dao
    def _animate(self):
        # Danh sách các sprite hoạt ảnh
        sprites = self.blade_img

        # Tính chỉ số sprite hiện tại (có vòng lặp nhờ phép toán modulo `%`)
        sprite_index = (self.frame_index // self.animation_delay) % len(sprites)

        # Cập nhật ảnh hiện tại dựa trên sprite_index
        self.image = sprites[sprite_index]

        # Tăng frame_index để chuyển sang khung hình tiếp theo
        self.frame_index += 1

        # Cập nhật lại vị trí của hình chữ nhật và mask
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        # Đặt lại frame_index nếu đã chạy hết tất cả các sprite
        if self.frame_index // self.animation_delay > len(sprites):
            self.frame_index = 0

    # Phương thức update: Cập nhật hoạt ảnh và vị trí bẫy khi màn hình cuộn
    def update(self, x_shift):
        self._animate()  # Gọi phương thức để cập nhật hoạt ảnh
        self.rect.x += x_shift  # Dịch chuyển vị trí của bẫy theo trục x với giá trị `x_shift`
