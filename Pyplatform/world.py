import pygame
from settings import tile_size, WIDTH  # Import kích thước ô gạch và chiều rộng màn hình
from tile import Tile  # Lớp Tile (gạch nền)
from trap import Trap  # Lớp Trap (bẫy)
from goal import Goal  # Lớp Goal (đích đến)
from player import Player  # Lớp Player (người chơi)
from game import Game  # Lớp Game (quản lý trạng thái trò chơi)

# Lớp World: Quản lý toàn bộ thế giới trò chơi
class World:
    def __init__(self, world_data, screen):
        self.screen = screen  # Màn hình hiển thị
        self.world_data = world_data  # Dữ liệu cấu trúc thế giới
        self._setup_world(world_data)  # Thiết lập thế giới từ dữ liệu
        self.world_shift = 0  # Tốc độ dịch chuyển thế giới
        self.current_x = 0  # Vị trí hiện tại của người chơi theo trục X
        self.gravity = 0.7  # Trọng lực
        self.game = Game(self.screen)  # Quản lý trạng thái trò chơi

    # Phương thức _setup_world: Tạo thế giới từ dữ liệu
    def _setup_world(self, layout):
        self.tiles = pygame.sprite.Group()  # Nhóm các ô gạch
        self.traps = pygame.sprite.Group()  # Nhóm các bẫy
        self.player = pygame.sprite.GroupSingle()  # Nhóm chứa người chơi (duy nhất một sprite)
        self.goal = pygame.sprite.GroupSingle()  # Nhóm chứa mục tiêu (đích đến)

        for row_index, row in enumerate(layout):  # Duyệt từng dòng trong dữ liệu
            for col_index, cell in enumerate(row):  # Duyệt từng ô trong dòng
                x, y = col_index * tile_size, row_index * tile_size  # Tính tọa độ
                if cell == "X":  # Gạch nền
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == "t":  # Bẫy
                    tile = Trap((x + (tile_size // 4), y + (tile_size // 4)), tile_size // 2)
                    self.traps.add(tile)
                elif cell == "P":  # Người chơi
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif cell == "G":  # Đích đến
                    goal_sprite = Goal((x, y), tile_size)
                    self.goal.add(goal_sprite)

    def reset_world(self):
        """Đặt lại toàn bộ thế giới"""
        self.__init__(self.world_data, self.screen)  # Tái khởi tạo lớp `World`

    def _handle_restart(self):
        keys = pygame.key.get_pressed()  # Lấy trạng thái phím
        if keys[pygame.K_RETURN]:  # Nếu nhấn phím "Enter"
            self.reset_world()

    # Phương thức _scroll_x: Dịch chuyển thế giới khi người chơi di chuyển
    def _scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < WIDTH // 3 and direction_x < 0:  # Người chơi ở gần biên trái
            self.world_shift = 8
            player.speed = 0
        elif player_x > WIDTH - (WIDTH // 3) and direction_x > 0:  # Người chơi ở gần biên phải
            self.world_shift = -8
            player.speed = 0
        else:  # Người chơi ở giữa màn hình
            self.world_shift = 0
            player.speed = 3

    # Phương thức _apply_gravity: Áp dụng trọng lực cho người chơi
    def _apply_gravity(self, player):
        player.direction.y += self.gravity  # Tăng tốc độ rơi
        player.rect.y += player.direction.y  # Cập nhật vị trí theo trọng lực

    # Phương thức _horizontal_movement_collision: Xử lý va chạm ngang
    def _horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed  # Di chuyển theo trục X

        for sprite in self.tiles.sprites():  # Kiểm tra va chạm với gạch nền
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:  # Va chạm khi di chuyển sang trái
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:  # Va chạm khi di chuyển sang phải
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    # Phương thức _vertical_movement_collision: Xử lý va chạm dọc
    def _vertical_movement_collision(self):
        player = self.player.sprite
        self._apply_gravity(player)  # Áp dụng trọng lực

        for sprite in self.tiles.sprites():  # Kiểm tra va chạm với gạch nền
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:  # Va chạm khi rơi xuống
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:  # Va chạm khi nhảy lên
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    # Phương thức _handle_traps: Xử lý khi người chơi va chạm bẫy
    def _handle_traps(self):
        player = self.player.sprite

        for sprite in self.traps.sprites():  # Kiểm tra va chạm với bẫy
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0 or player.direction.y > 0:
                    player.rect.x += tile_size
                elif player.direction.x > 0 or player.direction.y > 0:
                    player.rect.x -= tile_size
                player.life -= 1  # Giảm mạng sống của người chơi

    # Phương thức update: Cập nhật trạng thái thế giới và hiển thị
    def update(self, player_event):
        self._handle_restart()  # Kiểm tra và xử lý nhấn phím "Enter"

        # Cập nhật và hiển thị gạch nền
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.screen)

        # Cập nhật và hiển thị bẫy
        self.traps.update(self.world_shift)
        self.traps.draw(self.screen)

        # Cập nhật và hiển thị đích đến
        self.goal.update(self.world_shift)
        self.goal.draw(self.screen)

        self._scroll_x()  # Xử lý cuộn màn hình

        # Cập nhật và xử lý va chạm người chơi
        self._horizontal_movement_collision()
        self._vertical_movement_collision()
        self._handle_traps()
        self.player.update(player_event)
        self.game.show_life(self.player.sprite)  # Hiển thị mạng sống
        self.player.draw(self.screen)

        self.game.game_state(self.player.sprite, self.goal.sprite)  # Kiểm tra trạng thái trò chơi
