### A Flask implementation of the AirBnB_clone_v2
This README file serves as my practical introduction to Flask
so I would be documenting certain findings here
------------------------------------------------------------

MVC - Model - View - Controller

#### Model
The Model comprises of all the data, business logic layers, its guidelines and functions. The Model, upon getting user input data from the Controller, tells the way an updated interface should be displayed directly to the View.

#### View
The View is for the graphical representation of the data like graph or charts etc. It is the apps’ front-end. The View gets the user input and communicates the same to the Controller for examination and then update and reconstructs itself according to the Model’s instructions, or the Controller’s in case the modification requirement is minimum.

#### Controller
The Controller translates the input data into the scope of commands of the previous ones. It is the midway between the Model and the View. It gets the user input from the View; after processing it, the Controller notifies the Model (or View) of the changes required.
