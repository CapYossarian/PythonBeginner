import pyautogui
import math
import time
import random

# Настройки безопасности (прерывание при перемещении мыши в угол экрана)
pyautogui.FAILSAFE = True


def smooth_move(x, y, duration=1):
    """Плавное перемещение курсора к координатам (x, y) за указанное время."""
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)


def draw_circle(center_x, center_y, radius, steps=100):
    """Рисование круга с центром в (center_x, center_y)."""
    for i in range(steps + 1):
        angle = 2 * math.pi * i / steps
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        pyautogui.moveTo(x, y, duration=0.05)


def random_walk(steps=50, step_size=100):
    """Случайное блуждание курсора."""
    start_x, start_y = pyautogui.position()
    for _ in range(steps):
        dx = random.randint(-step_size, step_size)
        dy = random.randint(-step_size, step_size)
        smooth_move(start_x + dx, start_y + dy, duration=0.5)
        start_x, start_y = pyautogui.position()
        time.sleep(0.2)


if __name__ == "__main__":
    try:
        screen_width, screen_height = pyautogui.size()

        # Пример 1: Плавное перемещение по экрану
        smooth_move(screen_width // 2, screen_height // 2, duration=1)
        time.sleep(1)

        # Пример 2: Рисование круга
        draw_circle(screen_width // 2, screen_height // 2, radius=200)

        # Пример 3: Случайное движение
        random_walk(steps=120)

    except KeyboardInterrupt:
        print("\nСкрипт остановлен пользователем.")

# Чтобы остановить скрипт раньше времени:
# 1. Быстро переместите мышь в любой угол экрана (если FAILSAFE=True)
# 2. Или нажмите Ctrl+C в консоли