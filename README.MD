# contact_travel - Odoo Custom Module

## Overview
`contact_travel` is a custom Odoo module that adds travel tracking and a reward system to the standard Contacts app. It introduces a new model `Voyage` for tracking travel-related data and integrates it into the partner view with a smart button and computed fields.

## Features
- `Voyage` model to track user travels with name, date, destination, amount.
- Smart button on partner form showing number of voyages.
- Reward level field (`Argent`, `Or`, `Platine`) based on travel total.
- Explanation message for the reward level.
- Filtered voyage list per contact.

## Models
- `res.partner` (extended):
  - `voyage_ids`, `voyage_count`, `reward_level`, `explanation`
- `contact_travel.voyage`:
  - `name`, `departure_date`, `destination`, `partner_id`, `amount`

## Installation
1. Copy the module to your Odoo `addons` directory.
2. Restart the server.
3. Activate developer mode.
4. Install the module `contact_travel`.

## Usage
- Add some Contacts
- Add some Voyages.
- Go to a given contact.
- Open a contact form.
- Click the "Voyages de l'Utilisateur" button to see related voyages.
- Observe the reward level and explanation fields.

## License
MIT
