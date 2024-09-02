# Système de Gestion de Parking

Ce projet est un système de gestion de parking qui permet de gérer l'entrée, le paiement et la sortie des véhicules dans un parking.

## Fonctionnalités

- **Émission de Ticket** : Génération d'un ticket à l'entrée du parking.
- **Traitement de Paiement** : Gestion des paiements pour les places de parking.
- **Libération de Place** : Gestion de la sortie des véhicules et libération des places de parking.

## Commandes

- **IssueTicket** : Émission d'un ticket à l'entrée du parking.
- **ProcessPayment** : Traitement du paiement pour la place de parking.

## Événements

- **TicketIssued** : Émis quand un ticket est créé et une place est assignée.
- **PaymentReceived** : Émis quand un paiement est effectué avec succès.
- **SpaceFreed** : Émis quand un véhicule quitte le parking et la place devient disponible.

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votre-utilisateur/votre-repo.git
    ```
2. Accédez au répertoire du projet :
    ```sh
    cd votre-repo
    ```
3. Installez les dépendances :
    ```sh
    npm install
    ```

## Utilisation

1. Démarrez le serveur :
    ```sh
    npm start
    ```
2. Accédez à l'application via votre navigateur à l'adresse `http://localhost:3000`.

## Tests

Pour exécuter les tests unitaires, utilisez la commande suivante :
```sh
npm test
```

Pour tester votre API, vous pouvez utiliser un outil comme Postman ou simplement votre navigateur pour les requêtes GET. Voici comment vous pourriez tester différentes fonctionnalités :

1. **Ajouter un parking** : Faites une requête POST à `http://127.0.0.1:5000/parkings` avec un corps JSON contenant l'identifiant du parking, par exemple :
    ```json
    {
        "parking_id": "P1"
    }
    ```

2. **Entrer un véhicule** : Faites une requête POST à `http://127.0.0.1:5000/enter` avec les détails nécessaires, tels que :
    ```json
    {
        "parking_id": "P1",
        "vehicle_type": "voiture",
        "vehicle_plate": "ABC123"
    }
    ```

3. **Payer pour un stationnement** : Faites une requête POST à `http://127.0.0.1:5000/pay` avec les détails du ticket, par exemple :
    ```json
    {
        "parking_id": "P1",
        "space_id": "B1"
    }
    ```

4. **Sortir du parking** : Faites une requête POST à `http://127.0.0.1:5000/exit` avec les détails nécessaires, tels que :
    ```json
    {
        "parking_id": "P1",
        "space_id": "B1"
    }
    ```

5. **Voir l'historique** : Faites une requête GET à `http://127.0.0.1:5000/history/P1`.