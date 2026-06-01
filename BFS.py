from collections import deque

class BFSSolver:
    @staticmethod
    def solve_puzzle(initial_state, goal_state):
        # Initialisation de la file pour BFS
        queue = deque([initial_state])
        # Dictionnaire pour suivre d'où vient chaque état
        came_from = {initial_state: None}
        # Compteur d'itérations
        iterations = 0

        # Boucle principale : continuer jusqu'à ce que la file soit vide
        while queue:
            # Récupérer l'état au début de la file (FIFO)
            current_state = queue.popleft()
            # Incrémenter le compteur d'itérations
            iterations += 1

            # Vérifier si on a atteint l'état cible
            if current_state == goal_state:
                # Reconstituer le chemin en partant de l'état cible
                path = []
                while current_state in came_from:
                    path.insert(0, current_state)
                    current_state = came_from[current_state]
                return path, iterations

            # Générer les voisins de l'état actuel
            for next_state in BFSSolver.get_neighbors(current_state):
                # Si le voisin n'a pas encore été visité
                if next_state not in came_from:
                    # Ajouter le voisin à la file et enregistrer d'où il vient
                    queue.append(next_state)
                    came_from[next_state] = current_state

        # Si aucune solution n'a été trouvée, retourner None
        return None, iterations

    @staticmethod
    def get_neighbors(state):
        # Méthode pour générer les états voisins d'un état donné
        neighbors = []
        empty_tile_i, empty_tile_j = None, None
        # Trouver la position de la case vide
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    empty_tile_i, empty_tile_j = i, j

        # Générer les voisins en déplaçant la case vide
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
            # Vérifier si le déplacement est valide
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                # Créer un nouvel état en échangeant les cases
                new_state = [list(row) for row in state]
                new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
                neighbors.append(tuple(map(tuple, new_state)))

        return neighbors

