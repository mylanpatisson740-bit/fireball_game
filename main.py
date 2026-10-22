import sys
import os  # Utile pour les import de fichier permet d'afficher les images peu importe où le fichier est lancé

try:
    import pygame  # type: ignore[import-not-found]
except ImportError as exc:
    print("Erreur: la bibliothèque 'pygame' est absente. Installez-la avec 'pip install pygame'.")
    raise SystemExit(1) from exc

# --- Initialisation ---
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireball Game") # Titre

clock = pygame.time.Clock()
FPS = 60

# --- Couleurs ---
WHITE      = (255, 255, 255)
BLACK      = (0,   0,   0)
ORANGE     = (255, 140, 0)
YELLOW     = (255, 215, 0)
RED        = (200, 30,  30)
DARK_RED   = (139, 0,   0)
SKY_BLUE   = (135, 206, 235)
GRAY       = (100, 100, 100)

# --- Chargement des images ---
# Les images doivent être dans le même dossier que main.py
def load_image(filename, width, height):
    path = os.path.join(os.path.dirname(__file__), filename)
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, (width, height))

player_img  = load_image("arbre.png",  80, 100)
monster_img = load_image("mommy.png",  80, 100)
fond_img = load_image("fond.jpg", WIDTH, HEIGHT)
bdf_img=load_image("bdf.png",50, 70)


# ─────────────────────────────────────────
#  CLASSE PROJECTILE
# ─────────────────────────────────────────
class Projectile:
    def __init__(self, x, y):
        self.x      = x
        self.y      = y
        self.width  = 18
        self.height = 18
        self.speed  = 8
        self.active = True

    def update(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.active = False

    def draw(self, surface):
        surface.blit(bdf_img, (int(self.x) - 20, int(self.y) - 20))
        

    def get_rect(self):
        return pygame.Rect(self.x - self.width // 2,
                           self.y - self.height // 2,
                           self.width, self.height)


# ─────────────────────────────────────────
#  CLASSE PLAYER
# ─────────────────────────────────────────
class Player:
    def __init__(self, x, y):
        self.x           = x
        self.y           = y
        self.width       = 80
        self.height      = 100
        self.velocity    = 4   # ← modifier cette valeur pour changer la vitesse
        self.health      = 100
        self.attack      = 20
        self.projectiles = []

    def launch_projectile(self):
        proj = Projectile(self.x + self.width // 2 + 10,
                          self.y - self.height // 2)
        self.projectiles.append(proj)

    def update(self, keys):
        if keys[pygame.K_LEFT]  and self.x - self.velocity > 0:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x + self.velocity < WIDTH - self.width:
            self.x += self.velocity
        if keys[pygame.K_UP]    and self.y - self.velocity > self.height:
            self.y -= self.velocity
        if keys[pygame.K_DOWN]  and self.y + self.velocity < HEIGHT - 20:
            self.y += self.velocity

        for p in self.projectiles:
            p.update()
        self.projectiles = [p for p in self.projectiles if p.active]

    def draw(self, surface):
        # Image du joueur
        surface.blit(player_img, (self.x - self.width // 2,
                                  self.y - self.height))

        # Barre de vie
        bar_x = self.x - 30
        bar_y = self.y - self.height - 14
        pygame.draw.rect(surface, DARK_RED, (bar_x, bar_y, 60, 8))
        pygame.draw.rect(surface, RED,
                         (bar_x, bar_y, int(60 * self.health / 100), 8))

        for p in self.projectiles:
            p.draw(surface)

    def get_rect(self):
        return pygame.Rect(self.x - self.width // 2,
                           self.y - self.height,
                           self.width, self.height)


# ─────────────────────────────────────────
#  CLASSE MONSTER
# ─────────────────────────────────────────
class Monster:
    def __init__(self, x, y):
        self.x        = x
        self.y        = y
        self.width    = 80
        self.height   = 100
        self.velocity = 1
        self.health   = 100
        self.attack   = 100
        self.alive    = True

    def update(self, player_x):
        if self.x < player_x:
            self.x += self.velocity
        elif self.x > player_x:
            self.x -= self.velocity

    def draw(self, surface):
        if not self.alive:
            return

        # Image du monstre
        surface.blit(monster_img, (self.x - self.width // 2,
                                   self.y - self.height))

        # Barre de vie
        bar_x = int(self.x) - 30
        bar_y = int(self.y) - self.height - 14
        pygame.draw.rect(surface, DARK_RED, (bar_x, bar_y, 60, 8))
        pygame.draw.rect(surface, RED,
                         (bar_x, bar_y, int(60 * self.health / 100), 8))

    def get_rect(self):
        return pygame.Rect(self.x - self.width // 2,
                           self.y - self.height,
                           self.width, self.height)


# ─────────────────────────────────────────
#  DESSIN DU FOND
# ─────────────────────────────────────────
def draw_background(surface):
    surface.blit(fond_img, (0, 0))


# ─────────────────────────────────────────
#  AFFICHAGE HUD
# ─────────────────────────────────────────
font       = pygame.font.SysFont("Arial", 22, bold=True)
font_big   = pygame.font.SysFont("Arial", 48, bold=True)
font_small = pygame.font.SysFont("Arial", 16)

def draw_hud(surface, player, score):
    score_text = font.render(f"Score : {score}", True, BLACK)
    surface.blit(score_text, (10, 10))
    ctrl = font_small.render("Flèches : déplacer   |   Espace : boule de feu", True, GRAY)
    surface.blit(ctrl, (WIDTH // 2 - ctrl.get_width() // 2, HEIGHT - 38))

def draw_game_over(surface, score):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))
    txt = font_big.render("GAME OVER", True, RED)
    surface.blit(txt, (WIDTH // 2 - txt.get_width() // 2, HEIGHT // 2 - 60))
    s = font.render(f"Score final : {score}", True, WHITE)
    surface.blit(s, (WIDTH // 2 - s.get_width() // 2, HEIGHT // 2 + 10))
    r = font_small.render("Appuie sur R pour rejouer", True, WHITE)
    surface.blit(r, (WIDTH // 2 - r.get_width() // 2, HEIGHT // 2 + 55))


# ─────────────────────────────────────────
#  BOUCLE PRINCIPAL
# ─────────────────────────────────────────
def main():
    player    = Player(WIDTH // 4, HEIGHT - 60)
    monster   = Monster(WIDTH - 150, HEIGHT - 60)
    score     = 0
    game_over = False
    space_pressed = False

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    if not space_pressed:
                        player.launch_projectile()
                        space_pressed = True
                if event.key == pygame.K_r and game_over:
                    main()
                    return

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    space_pressed = False

        if not game_over:
            keys = pygame.key.get_pressed()
            player.update(keys)

            if monster.alive:
                monster.update(player.x)

                for proj in player.projectiles:
                    if proj.active and monster.get_rect().colliderect(proj.get_rect()):
                        proj.active = False
                        monster.health -= player.attack
                        if monster.health <= 0:
                            monster.health = 0
                            monster.alive  = False
                            score += 100

                if monster.get_rect().colliderect(player.get_rect()):
                    player.health -= 0.1
                    if player.health <= 0:
                        player.health = 0
                        game_over = True

            if not monster.alive:
                monster = Monster(WIDTH - 100, HEIGHT - 60)

        draw_background(screen)
        if monster.alive:
            monster.draw(screen)
        player.draw(screen)
        draw_hud(screen, player, score)
        if game_over:
            draw_game_over(screen, score)

        pygame.display.flip()


if __name__ == "__main__":
    main()
