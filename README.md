# libreoffice-macro-phonetic

Macro python pour libreoffice/openoffice permettant de récupérer la phonétique d'un mot depuis wordreference.com et la coller dans le document actif (Les scripts et docs sont basés sur libreoffice mais peuvent être réadaptés pour openoffice)

### Installation :

#### 🐧 Linux : 

 - S'assurer d'avoir une distribution python version 3.x et un Runtime Java installés
 - Lancer une fois libreoffice writer pour créer la configuration initiale
 - Exécuter le script `install-linux.sh`
 - Ajouter un raccourci clavier libreoffice exécutant la fonction `insert_phonetic()`

#### 🪟 Windows :

 - S'assurer d'avoir une distribution python version 3.x installée (avec l'option `Add to PATH` cochée pendant l'installation)
 - S'assurer d'avoir un Runtime Java (JRE) installé
 - Lancer une fois libreoffice writer pour créer la configuration initiale
 - Exécuter le script `install-windows.bat`
 - Ajouter un raccourci clavier libreoffice exécutant la fonction `insert_phonetic()`

### 🐞 Bugs connus
 - Quand l'ordinateur est connecté à un réseau sans avoir d'accès à Internet, libreoffice freeze pendant une quinzaine de secondes
- La phonétique d'un mot n'est pas rajoutée après, mais avant lui

### ☑ TODO
 - Ajouter la phonétique après le mot (la rajoute actuellement avant le mot sélectionné)
 - finaliser le script d'installation windows qui utilise la distribution python packagée avec libreoffice
