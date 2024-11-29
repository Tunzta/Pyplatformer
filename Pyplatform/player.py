import pygame
from support import import_sprite  # Import hàm hỗ trợ để tải các ảnh sprite

# Định nghĩa lớp Player đại diện cho người chơi trong trò chơi
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self._import_character_assets()  # Tải các tài nguyên hoạt ảnh của nhân vật
        self.frame_index = 0  # Chỉ số khung hình hiện tại
        self.animation_speed = 0.15  # Tốc độ chuyển đổi khung hình
        self.image = self.animations["idle"][self.frame_index]  # Hình ảnh ban đầu (trạng thái idle)
        self.rect = self.image.get_rect(topleft=pos)  # Vị trí khởi tạo của nhân vật
        self.mask = pygame.mask.from_surface(self.image)  # Tạo mask để kiểm tra va chạm chính xác

        # Thuộc tính di chuyển của người chơi
        self.direction = pygame.math.Vector2(0, 0)  # Vector hướng di chuyển
        self.speed = 5  # Tốc độ di chuyển
        self.jump_move = -16  # Lực nhảy

        # Trạng thái của người chơi
        self.life = 5  # Số mạng sống
        self.game_over = False  # Kiểm tra trạng thái kết thúc trò chơi
        self.win = False  # Kiểm tra trạng thái thắng
        self.status = "idle"  # Trạng thái hành động hiện tại
        self.facing_right = True  # Người chơi đang quay mặt sang phải
        self.on_ground = False  # Kiểm tra người chơi có đang chạm đất
        self.on_ceiling = False  # Kiểm tra người chơi có chạm trần
        self.on_left = False  # Kiểm tra người chơi có chạm tường trái
        self.on_right = False  # Kiểm tra người chơi có chạm tường phải

    # Hàm tải các tài nguyên hình ảnh (hoạt ảnh) cho nhân vật
    def _import_character_assets(self):
        character_path = "assets/player/"  # Đường dẫn thư mục chứa hình ảnh nhân vật
        self.animations = {
            "idle": [],
            "walk": [],
            "jump": [],
            "fall": [],
            "lose": [],
            "win": []
        }
        for animation in self.animations.keys():  # Lặp qua từng trạng thái để tải hình ảnh
            full_path = character_path + animation
            self.animations[animation] = import_sprite(full_path)

    # Hàm xử lý hoạt ảnh của người chơi
    def _animate(self):
        animation = self.animations[self.status]  # Lấy danh sách hình ảnh của trạng thái hiện tại

        # Chuyển đổi qua các khung hình
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):  # Nếu vượt quá số khung hình, quay lại khung đầu tiên
            self.frame_index = 0
        image = animation[int(self.frame_index)]  # Lấy khung hình hiện tại
        image = pygame.transform.scale(image, (35, 50))  # Điều chỉnh kích thước hình ảnh

        # Kiểm tra hướng của người chơi (trái/phải)
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)  # Lật hình ảnh theo chiều ngang
            self.image = flipped_image

        # Điều chỉnh vị trí của hình ảnh dựa trên trạng thái va chạm
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    # Hàm kiểm tra hành động di chuyển (trái/phải hoặc đứng yên)
    def _get_input(self, player_event):
        if player_event != False:
            if player_event == "right":  # Di chuyển sang phải
                self.direction.x = 1
                self.facing_right = True
            elif player_event == "left":  # Di chuyển sang trái
                self.direction.x = -1
                self.facing_right = False
        else:
            self.direction.x = 0  # Không di chuyển

    # Hàm xử lý hành động nhảy
    def _jump(self):
        self.direction.y = self.jump_move

    # Hàm xác định trạng thái hiện tại của người chơi
    def _get_status(self):
        if self.direction.y < 0:  # Đang nhảy
            self.status = "jump"
        elif self.direction.y > 1:  # Đang rơi
            self.status = "fall"
        elif self.direction.x != 0:  # Đang di chuyển
            self.status = "walk"
        else:  # Đứng yên
            self.status = "idle"

    # Hàm cập nhật trạng thái của người chơi
    def update(self, player_event):
        self._get_status()  # Xác định trạng thái hành động
        if self.life > 0 and not self.game_over:  # Kiểm tra nếu trò chơi chưa kết thúc
            if player_event == "space" and self.on_ground:  # Xử lý hành động nhảy
                self._jump()
            else:
                self._get_input(player_event)  # Xử lý di chuyển trái/phải
        elif self.game_over and self.win:  # Nếu trò chơi kết thúc và người chơi thắng
            self.direction.x = 0
            self.status = "win"
        else:  # Nếu thua
            self.direction.x = 0
            self.status = "lose"
        self._animate()  # Cập nhật hoạt ảnh của người chơi
