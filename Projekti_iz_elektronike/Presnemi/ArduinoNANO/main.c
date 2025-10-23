#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
  DDRD=255;
  while(1){
    for (int i=0; i<256; i++) {
      PORTD = i;
      _delay_ms(100);
    }
  }
}
