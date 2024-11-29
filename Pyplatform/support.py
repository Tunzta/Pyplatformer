from os import walk  # Thư viện để duyệt qua các tệp và thư mục
import pygame  # Thư viện chính để phát triển trò chơi

# Hàm import_sprite: Dùng để tải tất cả các ảnh sprite từ một thư mục cụ thể
def import_sprite(path):
    surface_list = []  # Danh sách để lưu các hình ảnh sprite đã tải

    # Duyệt qua các tệp trong đường dẫn (path)
    for _, __, img_file in walk(path):  # `walk` trả về (thư mục gốc, thư mục con, tệp trong thư mục)
        for image in img_file:  # Lặp qua từng tệp trong danh sách tệp
            full_path = f"{path}/{image}"  # Đường dẫn đầy đủ của từng tệp hình ảnh
            img_surface = pygame.image.load(full_path).convert_alpha()  # Tải ảnh và giữ alpha (nền trong suốt)
            surface_list.append(img_surface)  # Thêm ảnh vào danh sách

    return surface_list  # Trả về danh sách tất cả các ảnh sprite đã tải
