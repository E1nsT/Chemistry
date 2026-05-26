import pygame
import random
import math

pygame.init()

font = pygame.font.SysFont(None, 36)

WIDTH = 600
HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

reaction_counter = 0 

class Particle:
    def __init__(self, x, y, type, color):
        self.x = x
        self.y = y
        self.type = type
        self.color = color
        self.vx = random.uniform(-0.5,0.5)
        self.vy = random.uniform(-0.5,0.5)
        self.reacted = False
    
    def move(self):
            self.x += self.vx
            self.y += self.vy

            if self.x < 0:
                 self.x = 0
                 self.vx = -self.vx

            elif self.x > WIDTH:
                 self.x = WIDTH
                 self.vx = -self.vx

            if self.y < 0:
                 self.y = 0
                 self.vy = -self.vy

            elif self.y > HEIGHT:
                 self.y = HEIGHT
                 self.vy = -self.vy

    def draw(self, screen):
        if self.type == "acid":
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
        if self.type == "base":
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)


def collide(particles):
     global reaction_counter

     for i in range(len(particles)):
          for j in range(i + 1, len(particles)):
               
               p1 = particles[i]
               p2 = particles[j]

               if p1.type != p2.type and not p1.reacted and not p2.reacted:
                    dx = p1.x - p2.x
                    dy = p1.y - p2.y
                    distance = math.sqrt(dx*dx + dy*dy)

                    if distance < 5:
                         reaction_counter +=1
                         p1.reacted = True
                         p2.reacted = True

def create_particles(concentration):
    acid_particles = int(concentration * 50)
    base_particles = 50

    for i in range(acid_particles):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        particles.append(Particle(x, y, "acid", (255, 0, 0)))

    for i in range(base_particles):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        particles.append(Particle(x, y, "base", (0, 255, 0)))


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Theory")
particles = []
create_particles(1)

clock = pygame.time.Clock()
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        for p in particles:
             p.move()

            
        collide(particles)

        if not any(p.type == "acid" and not p.reacted for p in particles):
             running = False
        if not any(p.type == "base" and not p.reacted for p in particles):
             running = False

        for p in particles:
             p.draw(screen)

        reaction_text = font.render(f"Collisions: {reaction_counter}", True, BLACK)
        screen.blit(reaction_text, (10, 10))


        pygame.display.update()
        clock.tick(60)

pygame.quit()
