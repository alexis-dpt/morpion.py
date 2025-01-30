import pygame
import sys

Créateur = "alexis_dpt_on_github"
print(Créateur)

pygame.init()

taille_fenetre = 450
fenetre = pygame.display.set_mode((taille_fenetre, taille_fenetre))
pygame.display.set_caption("Morpion | Crée par alexis_dpt 🤓 | Version 1.5")

grille = [[None, None, None], [None, None, None], [None, None, None]]
tour = "X"
jeu_fini = False
mode_de_jeu = None

def dessiner_grille():
    for x in range(1, 3):
        pygame.draw.line(fenetre, (255, 255, 255), (x * taille_fenetre // 3, 0), (x * taille_fenetre // 3, taille_fenetre))
        pygame.draw.line(fenetre, (255, 255, 255), (0, x * taille_fenetre // 3), (taille_fenetre, x * taille_fenetre // 3))

def verifier_victoire():
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] and grille[i][0] is not None:
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] is not None:
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] is not None:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] is not None:
        return True
    return False

def afficher_notification(gagnant):
    fenetre.fill((0, 0, 0))
    font = pygame.font.Font(None, 60)
    texte = font.render(f"Joueur {gagnant} a gagné!", True, (255, 255, 255))
    fenetre.blit(texte, (taille_fenetre // 2 - texte.get_width() // 2, taille_fenetre // 2 - texte.get_height() // 2 - 50))
    
    bouton_rejouer = pygame.Rect(taille_fenetre // 2 - 100, taille_fenetre // 2 + 20, 200, 50)
    bouton_menu = pygame.Rect(taille_fenetre // 2 - 100, taille_fenetre // 2 + 80, 200, 50)
    
    pygame.draw.rect(fenetre, (255, 0, 0), bouton_rejouer)
    pygame.draw.rect(fenetre, (0, 255, 0), bouton_menu)
    
    font = pygame.font.Font(None, 36)
    texte_rejouer = font.render("Rejouer", True, (255, 255, 255))
    texte_menu = font.render("Menu principal", True, (255, 255, 255))
    
    fenetre.blit(texte_rejouer, (bouton_rejouer.x + (200 - texte_rejouer.get_width()) // 2, bouton_rejouer.y + 10))
    fenetre.blit(texte_menu, (bouton_menu.x + (200 - texte_menu.get_width()) // 2, bouton_menu.y + 10))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_rejouer.collidepoint(event.pos):
                    return "rejouer"
                elif bouton_menu.collidepoint(event.pos):
                    return "menu"

def afficher_égalité():
    while True:
        fenetre.fill((0, 0, 0))
        font = pygame.font.Font(None, 60)
        texte = font.render("Égalité!", True, (255, 255, 255))
        fenetre.blit(texte, (taille_fenetre // 2 - texte.get_width() // 2, taille_fenetre // 2 - texte.get_height() // 2 - 50))

        bouton_rejouer = pygame.Rect(taille_fenetre // 2 - 100, taille_fenetre // 2 + 20, 200, 50)
        bouton_menu = pygame.Rect(taille_fenetre // 2 - 100, taille_fenetre // 2 + 80, 200, 50)

        pygame.draw.rect(fenetre, (255, 0, 0), bouton_rejouer)
        pygame.draw.rect(fenetre, (0, 255, 0), bouton_menu)

        font = pygame.font.Font(None, 36)
        texte_rejouer = font.render("Rejouer", True, (255, 255, 255))
        texte_menu = font.render("Menu principal", True, (255, 255, 255))

        fenetre.blit(texte_rejouer, (bouton_rejouer.x + (200 - texte_rejouer.get_width()) // 2, bouton_rejouer.y + 10))
        fenetre.blit(texte_menu, (bouton_menu.x + (200 - texte_menu.get_width()) // 2, bouton_menu.y + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_rejouer.collidepoint(event.pos):
                    return "rejouer"
                if bouton_menu.collidepoint(event.pos):
                    return "menu"

def afficher_menu_principal():
    fenetre.fill((0, 0, 0))
    font = pygame.font.Font(None, 60)
    texte = font.render("Morpion Alexis", True, (255, 255, 255))
    fenetre.blit(texte, (taille_fenetre // 2 - texte.get_width() // 2, taille_fenetre // 2 - texte.get_height() // 2 - 120))
    
    bouton_jouer = pygame.Rect(taille_fenetre // 2 - 100, taille_fenetre // 2 - 40, 200, 50)
    
    pygame.draw.rect(fenetre, (255, 0, 0), bouton_jouer)
    
    font = pygame.font.Font(None, 36)
    texte_jouer = font.render("Jouer", True, (255, 255, 255))
    
    fenetre.blit(texte_jouer, (bouton_jouer.x + (200 - texte_jouer.get_width()) // 2, bouton_jouer.y + 10))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_jouer.collidepoint(event.pos):
                    return "jouer"

def afficher_menu_modes():
    fenetre.fill((0, 0, 0))
    font = pygame.font.Font(None, 60)
    texte = font.render("Sélectionnez le mode", True, (255, 255, 255))
    fenetre.blit(texte, (taille_fenetre // 2 - texte.get_width() // 2, taille_fenetre // 2 - texte.get_height() // 2 - 120))
    
    bouton_mode1 = pygame.Rect(taille_fenetre // 2 - 100, taille_fenetre // 2 - 40, 200, 50)
    bouton_mode2 = pygame.Rect(taille_fenetre // 2 - 100, taille_fenetre // 2 + 20, 200, 50)
    
    pygame.draw.rect(fenetre, (0, 255, 0), bouton_mode1)
    pygame.draw.rect(fenetre, (0, 0, 255), bouton_mode2)
    
    font = pygame.font.Font(None, 30)
    texte_mode1 = font.render("Humain vs Humain", True, (255, 255, 255))
    texte_mode2 = font.render("Humain vs Ordinateur (bientôt)", False, (255, 255, 255))
    
    fenetre.blit(texte_mode1, (bouton_mode1.x + (200 - texte_mode1.get_width()) // 2, bouton_mode1.y + 10))
    fenetre.blit(texte_mode2, (bouton_mode2.x + (200 - texte_mode2.get_width()) // 2, bouton_mode2.y + 10))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_mode1.collidepoint(event.pos):
                    return "mode1"
                elif bouton_mode2.collidepoint(event.pos):
                    print("Pas le temps de coder l'ordinateur 😅")
                    return "non_disponible"

while True:
    choix_menu = afficher_menu_principal()
    if choix_menu == "jouer":
        mode_de_jeu = afficher_menu_modes()
    if mode_de_jeu in ["mode1", "mode2"]:
        print(f"Mode {mode_de_jeu} sélectionné")
        jeu_fini = False
        grille = [[None, None, None], [None, None, None], [None, None, None]]
        tour = "X"
        while not jeu_fini:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not jeu_fini:
                    x, y = event.pos
                    col = x // (taille_fenetre // 3)
                    row = y // (taille_fenetre // 3)
                    if grille[row][col] is None:
                        grille[row][col] = tour
                        if verifier_victoire():
                            resultat = afficher_notification(tour)
                            if resultat == "rejouer":
                                grille = [[None, None, None], [None, None, None], [None, None, None]]
                                tour = "X"
                                jeu_fini = False
                            elif resultat == "menu":
                                jeu_fini = True
                        tour = "O" if tour == "X" else "X"
            
            fenetre.fill((0, 0, 0))
            dessiner_grille()
            for row in range(3):
                for col in range(3):
                    if grille[row][col] is not None:
                        pos_x = col * taille_fenetre // 3 + taille_fenetre // 6
                        pos_y = row * taille_fenetre // 3 + taille_fenetre // 6
                        font = pygame.font.Font(None, 80)
                        texte = font.render(grille[row][col], True, (255, 255, 255))
                        fenetre.blit(texte, (pos_x - texte.get_width() // 2, pos_y - texte.get_height() // 2))
            pygame.display.flip()
            