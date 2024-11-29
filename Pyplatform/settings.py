# world_map: Bản đồ của thế giới trong trò chơi, được định nghĩa bằng chuỗi ký tự.
# Mỗi ký tự đại diện cho một loại đối tượng hoặc không gian trong trò chơi:
# - ' ': Không gian trống (nền trời hoặc không có vật cản).
# - 'X': Gạch hoặc nền tảng mà người chơi hoặc đối tượng khác có thể đứng lên.
# - 'P': Vị trí bắt đầu của người chơi (Player).
# - 'G': Cổng đích (Goal) để hoàn thành màn chơi.
# - 't': Cây hoặc vật trang trí khác.
# - 's': Gạch đặc biệt hoặc điểm nhấn (ví dụ: điểm dừng hoặc đối tượng đặc biệt khác).

world_map = [
    '                                                                  ',
    '                                                                  ',
    '                t  t                                              ',
    '        X     XXXXXXXXXs                   XX   X                 ',
    ' tXXXt     XX         XX                XXXX tt XX                ',
    ' XX XX                                      XXXXX                 ',
    '          Xt    t           t  t   X                            G ',
    '        XXXXXX  XXXXs    XXXXXXXXXXX  XX              tt t     XXX',
    ' P   XX  X XX X  X XXXt     X XX  XX  XXX  XXXXXXXXs  XXXXXX      ',
    'XXXXXXX  X  X X  X  XXXXXXXXX XX  XX  XXX  XX XX XXXXXXX  X       ',
]

# Kích thước của mỗi ô (tile) trong bản đồ.
tile_size = 50  # Mỗi ô có kích thước 50x50 pixel.

# Chiều rộng (WIDTH) và chiều cao (HEIGHT) của cửa sổ trò chơi:
# - WIDTH: Chiều rộng cố định của cửa sổ trò chơi, 1000 pixel.
# - HEIGHT: Chiều cao được tính dựa trên số hàng trong world_map nhân với tile_size.
WIDTH, HEIGHT = 1000, len(world_map) * tile_size
