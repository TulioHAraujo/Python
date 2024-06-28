"""
Ex021
Faça um programa que abra e reproduza um áudio de um arquivo mp3.
Difícil.

Esse exercício foi bem complexo no meu entendimento, a biblioteca não está tão atualizada
e sua sintaxe é complexa, consegui resolver apenas assistindo à aula.
Mas foi válido, porque fiz algumas pesquisas.
"""
import pygame

pygame.init()

pygame.mixer.music.load('Vlad-Gluschenko-Summer-Goes.mp3')
pygame.mixer.music.play()
input() #input() antes da linha abaixo, por isso não estava tocando.
pygame.event.wait()
