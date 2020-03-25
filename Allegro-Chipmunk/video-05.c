
#include <allegro5/allegro.h>
#include <allegro5/allegro_primitives.h>
#include <stdio.h>
#include <math.h>

#define true 1
#define false 0

void move_circle(float* x, float* y, float velX, float velY) {
	
	float x_dist = velX - *x;
	float y_dist = velY - *y;

	float distance = sqrt(x_dist * x_dist + y_dist * y_dist);

	if (distance > 1) {
		*x += x_dist * 0.001;
		*y += y_dist * 0.001;
	}
}

int main() {

	if (!al_init()) { return -1; }

	ALLEGRO_DISPLAY* display = al_create_display(1280, 720);

	if (!display) { return -1; }

	if (!al_init_primitives_addon()) { return -1; }

	al_install_mouse();

	int running = true;
	float cx = 0;
	float cy = 0;
	float velX = 0;
	float velY = 0;
	int click_once = true;

	ALLEGRO_EVENT event;
	ALLEGRO_EVENT_QUEUE* event_queue = al_create_event_queue();
	al_register_event_source(event_queue, al_get_display_event_source(display));
	al_register_event_source(event_queue, al_get_mouse_event_source());

	ALLEGRO_MOUSE_STATE mouse_state;


	while (running) {

		al_get_next_event(event_queue, &event);
		if (event.type == ALLEGRO_EVENT_DISPLAY_CLOSE) { running = false; }
		else if (event.type == ALLEGRO_EVENT_MOUSE_AXES) {
			
			velX = event.mouse.x;
			velY = event.mouse.y;
		}

		al_get_mouse_state(&mouse_state);
		/*
		if (al_mouse_button_down(&mouse_state, 1) && click_once) {
			printf("Mouse press: (%d, %d)\n", mouse_state.x, mouse_state.y);
			click_once = false;
		}
		else if (!al_mouse_button_down(&mouse_state, 1) && !click_once) {
			printf("Mouse release: (%d, %d)\n", mouse_state.x, mouse_state.y);
			click_once = true;
		}*/

		if (event.type == ALLEGRO_EVENT_MOUSE_BUTTON_DOWN && click_once) {
			if (mouse_state.buttons & 1) {
				printf("Mouse position press: (%d, %d)\n", event.mouse.x, event.mouse.y);
				click_once = false;
			}
		}
		else if (event.type == ALLEGRO_EVENT_MOUSE_BUTTON_UP && !click_once) {
			if (!(mouse_state.buttons & 1)) {
				printf("Mouse position release: (%d, %d)\n", event.mouse.x, event.mouse.y);
				click_once = true;
			}
		}

		move_circle(&cx, &cy, velX, velY);

		// Draw here
		al_clear_to_color(al_map_rgb(0, 0, 0));

		al_draw_circle(cx, cy, 50, al_map_rgb(255, 0, 0), 2);
		al_draw_filled_circle(200, 200, 50, al_map_rgb(255, 150, 0));

		al_draw_rectangle(300, 300, 350, 350, al_map_rgb(0, 150, 0), 2);
		al_draw_filled_rectangle(400, 400, 500, 500, al_map_rgb(0, 250, 120));
		al_draw_rounded_rectangle(550, 500, 650, 600, 10, 10, al_map_rgb(255, 150, 255), 2);

		al_draw_filled_triangle(640, 360, 740, 360, 690, 310, al_map_rgb(0, 100, 200));


		al_flip_display();


	}

	al_destroy_display(display);
	return 0;
}