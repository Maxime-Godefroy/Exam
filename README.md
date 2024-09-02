# Système de Gestion de Parking

Ce projet est un système de gestion de parking qui permet de gérer l'entrée, le paiement et la sortie des véhicules dans un parking.

## 1. Entités et Value Objects

### Entités
- **ParkingLot** : Un parking unique identifiable par son ID.
- **ParkingSpace** : Place de parking identifiable par une combinaison de lettre et numéro (ex. A1, B3).
- **Ticket** : Ticket émis pour un stationnement, contenant les détails du véhicule, le prix, le statut de paiement, et l'emplacement.

### Value Objects
- **Vehicle** : Détails du véhicule incluant le type et la plaque d'immatriculation. Pas d'identité propre dans le système.
- **Price** : Coût associé à chaque type de véhicule pour le stationnement.
- **PaymentRecord** : Enregistre les détails d'un paiement, incluant le montant et la date.

## 2. Bounded Contexts

- **Parking Management**
  - Gestion des parkings, allocation des places, et suivi des espaces disponibles.
- **Ticketing System**
  - Gestion de l'émission, du paiement et de la validation des tickets.
- **Payment Processing**
  - Traitement des paiements et enregistrement des transactions.

## 3. Acteurs, Commandes et Events

### Acteurs
- **Client** : Utilisateur qui engage des interactions pour obtenir et payer des tickets de parking.

### Commandes
- **IssueTicket** : Émission d'un ticket à l'entrée du parking.
- **ProcessPayment** : Traitement du paiement pour la place de parking.

### Events
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