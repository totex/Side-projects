

#ifdef MATHLIBRARY_EXPORTS
#define MATHLIBRARY_API __declspec(dllexport)
#else
#define MATHLIBRARY_API __declspec(dllimport)
#endif


MATHLIBRARY_API double sinus(double num);

MATHLIBRARY_API double cosinus(double num);

