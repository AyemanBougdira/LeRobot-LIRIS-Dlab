# conda create -y -n aloha python=3.10
# conda activate aloha
# pip install gym-aloha


# example.py
import imageio
import gymnasium as gym
import numpy as np
import gym_aloha

# imageio: Permet de lire et écrire des images et des vidéos.
# gymnasium(gym): Une bibliothèque utilisée pour créer des environnements simulés pour les algorithmes d'apprentissage par renforcement.
# numpy(np): Bibliothèque pour la manipulation de tableaux de données numériques.
# gym_aloha: Une bibliothèque personnalisée contenant des environnements spécifiques basés sur le protocole Aloha.

env = gym.make("gym_aloha/AlohaInsertion-v0")

# gym.make(...) : Initialise un environnement spécifique défini par "gym_aloha/AlohaInsertion-v0".

observation, info = env.reset()
frames = []

# env.reset(): Réinitialise l'environnement au début d'un épisode. Cela retourne l'observation initiale et des informations additionnelles(info).
# frames = []: Initialise une liste vide pour stocker les images(frames) de la simulation.

for _ in range(100):
    action = env.action_space.sample()

    # env.action_space.sample() : Choisit une action aléatoire parmi l'espace d'actions disponibles de l'environnement.
    # env.action_space est l'espace des actions possibles que l'agent peut effectuer dans l'environnement.
    observation, reward, terminated, truncated, info = env.step(action)
    # env.step(action): Exécute l'action choisie dans l'environnement et retourne:
    # observation: L'observation après avoir exécuté l'action.
        #reward: La récompense obtenue pour cette action.
        #terminated: Un booléen indiquant si l'épisode est terminé.
        #truncated: Un booléen indiquant si l'épisode a été interrompu(par exemple, pour une raison de temps).
        #info: Informations supplémentaires sur l'étape.
    image = env.render()
    frames.append(image)
    # env.render(): Génère une image représentant l'état actuel de l'environnement.
    # frames.append(image): Ajoute l'image à la liste des frames pour créer la vidéo plus tard.

    if terminated or truncated:
        observation, info = env.reset()

        # Si l'épisode est terminé (terminated) ou interrompu (truncated), l'environnement est réinitialisé en appelant env.reset().

env.close()
imageio.mimsave("example10.mp4", np.stack(frames), fps=25)


