import rerun as rr  # NOTE: `rerun`, not `rerun-sdk`!
import numpy as np



rr.init("rerun_example_my_data", spawn=True)

# rr.init(...): Cette fonction initialise une session Rerun.
# spawn=True indique qu'une nouvelle fenêtre de visualisation doit être lancée.


positions = np.zeros((10, 3))

# On crée un tableau de 10 points, chacun ayant une position en 3D (x, y, z).
# Tous les points sont initialisés à (0, 0, 0).



positions[:, 0] = np.linspace(-10, 10, 10)

# On modifie la coordonnée x des points en utilisant np.linspace, qui génère 10 valeurs régulièrement espacées entre -10 et 10.
# Les coordonnées y et z restent à 0, donc les points sont alignés sur l'axe des x.



colors = np.zeros((10, 3), dtype=np.uint8)
colors[:, 0] = np.linspace(0, 255, 10)

rr.log(
    "my_points",
    rr.Points3D(positions, colors=colors, radii=0.5)
)
