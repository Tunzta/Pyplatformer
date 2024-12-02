# world_map: Bản đồ của thế giới trong trò chơi, được định nghĩa bằng chuỗi ký tự.
# Mỗi ký tự đại diện cho một loại đối tượng hoặc không gian trong trò chơi:
# - ' ': Không gian trống (nền trời hoặc không có vật cản).
# - 'X': Gạch hoặc nền tảng mà người chơi hoặc đối tượng khác có thể đứng lên.
# - 'P': Vị trí bắt đầu của người chơi (Player).
# - 'G': Cổng đích (Goal) để hoàn thành màn chơi.
# - 't': Cây hoặc vật trang trí khác.
# - 's': Gạch đặc biệt hoặc điểm nhấn (ví dụ: điểm dừng hoặc đối tượng đặc biệt khác).
# - 'c': Vị trí của đồng xu.

world_map = [
    ' ' * 240,
    ' ' * 240,
    '                t ctc        t      cc           c    c            c                           c cc  cc  ',
    '        X     XXXXXXXXXs  X  XX    XXX           XX   X     c   X       X       X  c   X       XX XX XX  ',
    ' tXXXt     XX      c  XX                XXXX ttcXX   c            c                XXXXXX XX X           ',
    ' XX XX                                      XXXXX         tc      X  X     c   Xtt  X      c            G',
    '      c   Xtc   t     c     t c t   X         c        XXXXX  X           X  tXt    X   tXc  t ct  XXX  X',
    '        XXXXXX  XXXXs    XXXXXXXXXXX  XX    c     tct     XXX   X  XX X      ttt  XXXXXX  XX cXXXXs      ',
    ' P   XX  X XX X  X XXXt     X XX  XX  XXX  XXXXXXXXs  XXXXXX     c        t   XXXXXXXXXXXXX  XX          ',
    'XXXXXXX  X  X X  X  XXXXXXXXX XX  XX  XXX  XX XX XXXXXXX  X     XX  X         tt   XX X  X    XXXXXX     ',
]




# Kích thước của mỗi ô (tile) trong bản đồ.
tile_size = 50  # Mỗi ô có kích thước 50x50 pixel.

# Chiều rộng (WIDTH) và chiều cao (HEIGHT) của cửa sổ trò chơi:
# - WIDTH: Chiều rộng cố định của cửa sổ trò chơi, 1000 pixel.
# - HEIGHT: Chiều cao được tính dựa trên số hàng trong world_map nhân với tile_size.
WIDTH, HEIGHT = 1000, len(world_map) * tile_size
