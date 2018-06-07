# Все используемые константы (то, что никак не меняется где бы то ни было)
win_w = 800  # Ширина окна
win_h = int(3 * win_w / 4)  # Высота окна
scaling = win_w / 800  # Масштаб (все константы лучше задавать через него. Например: spd = 7 * scaling)
bull_w = 50  # Размер пули (диаметр)
bonus_w = 60  # Размер бонуса (диаметр

# Константы, необходимые для отрисовки самолётика
pl_w = 150 * scaling  # Ширина фигуры самолётика
pl_h = pl_w / 3  # Высота фигуры самолётика

midle_x = (win_w - pl_w) / 2  # Координаты самолётика, при которых он отобр. в центре экрана
midle_y = (win_h - pl_h) / 2
pl_x0 = midle_x  # Стартовыеоординаты самолётика
pl_y0 = midle_y
bull_w = 55 * scaling  # Размер пули (диаметр)
bonus_w = 55 * scaling  # Размер бонуса (диаметр
bullet_speed_init = 4.6 * scaling
bullet_speed_add = 0.7 * scaling

bonus_speed = 5 * scaling  # скорость +life можем менять
t_ext = 23  # время, через которое выпускается новый бонус ЖИЗНЬ. можно редактировать
n_ext = 1  # количество бонусов ЖИЗНЬ, сгенерированных за игру
t_vpn = 17  # время, через которое выпускается новый бонус VPN. можно редактировать
n_vpn = 1  # количество бонусов VPN, сгенерированных за игру

spd = 7 * scaling  # Скорость самолетика вдоль оси OX
pl_g = 0.5 * scaling  # Ускорение свободного самолёта
a_down = pl_g * 1.2  # Ускорение самолета при движении вниз
shell_r = 3 * scaling  # Радиус снаряда
delay = 17
t = 1  # Время одного движения
spd_up = -8 * scaling  # Скорость, приобретаемая при движении вверх

invulnerability_t = 100  # Время неуязвимости после потери жизни
invulnerability_t_damage = 100
invulnerability_t_bonus = 600

t_vul = 0  # Счетчик который отвечает за учет invulnerability_t в процедуре check_lives()
t_add = 5  # Для счетчика , можно изменять в зависимости от того, сколько должен самолет быть неуязвимым
rescue_spd = 2 * spd

# Необходимо ограничить движение самолётика вдоль оси Х
brd = spd  # min расстояние на которое самолетик может приблизится к краям экрана

# Константы, необходимые для отрисовки облаков
cld_w = int(160 * scaling)
cld_h = int(103 * scaling)
shift = int(0.3 * cld_h)

cld_border_shift = cld_w * 0.5

cld_v = 3.5 * scaling  # Скорость движения облаков, с ней можно играться

speed_counter_lim = 5000  # Предел увеличения скорости пуль
