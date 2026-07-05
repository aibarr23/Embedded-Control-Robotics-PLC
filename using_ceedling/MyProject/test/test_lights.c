
#ifdef TEST

#include "unity.h"

#include "lights.h"

void setUp(void)
{
}

void tearDown(void)
{
}

void test_WhenTheHeadlightSwitchIsOn_ThenTheHeadLightsAreOn(void){
    lights_SetHeadlightSwitchOn();
    TEST_ASSERT_EQUAL(true, lights_AreHeadlightsOn());
}

void test_WhenTheHeadlightSwitchIsOFF_ThenTheHeadLightsAreOff(void){
    // when the headlight switch is off..
    lights_SetHeadlightSwitchOff();

    // then the headlights are off
    TEST_ASSERT_EQUAL(false, lights_AreHeadlightsOn());
}


#endif // TEST
