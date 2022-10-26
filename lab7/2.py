#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)

# =======================================================================================
# Class of 2-dim vectors
# =======================================================================================
class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        """"возвращает разность двух векторов"""
        return Vec2d(self.x - other.x, self.y - other.y)


    def __add__(self, other):
        """возвращает сумму двух векторов"""
        return Vec2d(self.x + other.x, self.y + other.y)


    def __length__(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y + self.y)


    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return Vec2d(self.x * k, self.y * k)


    def int_pair(self):
        return (self.x, self.y)


# =======================================================================================
# Classes of lines
# =======================================================================================
class Polyline():
    def __init__(self):
        self.steps = 35
        self.pt = []
        self.spd = []
    

    def add_pt(self, point, speed):
        self.pt.append(point)
        self.spd.append(speed)


    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.pt)):
            self.pt[p] += self.spd[p]
            if self.pt[p].x > SCREEN_DIM[0] or self.pt[p].x < 0:
                self.spd[p] = Vec2d(- self.spd[p].x, self.spd[p].y)
            if self.pt[p].y > SCREEN_DIM[1] or self.pt[p].y < 0:
                self.spd[p] = Vec2d(self.spd[p].x, -self.spd[p].y)
    

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            pts = Knot().get_knot(self.pt, self.steps)
            for p_n in range(-1, len(pts) - 1):
                pygame.draw.line(gameDisplay, color, pts[p_n].int_pair(), pts[p_n + 1].int_pair(), width)
        elif style == "points":
            for p in self.pt:
                pygame.draw.circle(gameDisplay, color, p.int_pair(), width)


class Knot(Polyline):
    def get_point(self, alpha, deg=None):
        if deg is None:
            deg = len(self.pt) - 1
        if deg == 0:
            return self.pt[0]
        return self.pt[deg] * alpha + Knot().get_point(self.pt, alpha, deg - 1) * (1 -alpha)


    def get_points(self, basis_pts, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(Knot().get_point(basis_pts, i * alpha))
        return res


    def get_knot(self, points, count):
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append((points[i] + points[i + 1]) * 0.5)
            ptn.append(points[i + 1])
            ptn.append((points[i + 1] + points[i + 2]) * 0.5)
            res.extend(Knot().get_points(ptn, count))
        return res


# =======================================================================================
# Функции отрисовки
# =======================================================================================
def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(line.steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True
    show_help = False
    pause = True
    line = Polyline()

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    line = Polyline()
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    line.steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    line.steps -= 1 if line.steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                line.add_pt(Vec2d(event.pos[0], event.pos[1]), Vec2d(random.random))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        line.draw_points(3, color)
        if not pause:
            line.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
