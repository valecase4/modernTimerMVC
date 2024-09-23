# Modern Timer in Tkinter Python

## Approach: MVC Design Pattern

### Model

Model implement different methods that acts on its attributes "seconds" and "is_running".

For instance: run_timer() method set the attribute "is_running" to True. 

Both "seconds" attribute and "is_running" attribute are used by the controller. 

### View: see demo.png

View is divided into different components. 
Look at design.jpg to understand better how the view has been organized.

Main Frame --> top Frame
               mid Frame

mid Frame --> Mid Frame Left
              Mid Frame Right

Mid Frame Left displays the flow of time.
Mid Frame Right display the flow of time through a time circle.

### Controller

Controller component is splitted into different sub-components.

- startBtnController: communicate with startBtn component defined in the view. 
- pauseBtnController: communicate with pauseBtn component defined in the view.
- resetBtnController: communicate with resetBtn component defined in the view

These are the controllers for the main buttons. Basically, they manage the state of these buttons (disabled or not).

- minuteBtnController: communicate with minuteBtn component defined in the view. There are 5 minute buttons in the window:
1 mins, 5 mins, 10 mins, 20 mins and 60 mins. This component manages the state (disabled or not) of these buttons.

- timerLabelController: communicate with timerLabel component defined in the view, that displays the flow of time to the user. For this reason, this component has to be updated. Its controller manages the updates. 

The main controller component implements all these sub-components and communicates with the model. 

In particular, the main controller implements four methods:
- on_click_start_btn() --> manages the behavior of the application when the user clicks on start button
- on_click_pause_btn() --> manages the behavior of the application when the user clicks on the pause button
- on_click_reset_btn() --> manages the behavior of the application when the user clicks on the reset button
- on_click_minute_btn() --> manages the behavior of the application when one of the minute buttons is clicked.

### Workflow, example: User clicks on start button

The click on the start button means that the timer has to start. 

What happens when this button is clicked?

1. Get the current seconds. Are they greater than 0? If not, a pop-up is displayed to the user
2. If yes, if timer isn't running yet, the controller communicates with the model and the model.is_running attribute is setted to True. 
3. Consequently, controller.is_running attribute is setted to True
It means that the timer is ready to run.
4. It communicates with the timer label controller to update the flow of time displayed to the user.
5. It manages the behavior of the other buttons. For instance, when timer is running, the reset button is disabled.

