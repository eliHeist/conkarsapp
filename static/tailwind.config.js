module.exports = {
    content: ['../templates/*.html', '../**/templates/**/*.html'],
    darkMode: 'media', // or 'class'
    theme: {
        extend: {
            colors: {
                primary: {
                    100: '#064623',
                    500: '#46E317',
                },
                secondary: {
                    100: '#BDDADF',
                    500: '#00e5ff',
                    700: '#16bfd2',
                    900: '#0d1515',
                },
                dark: {
                    100: '#1E1E1E',
                    200: '#202020'
                },
                lead: '#AEAEAE',
                grey: {
                    50: 'rgb(252, 252, 252)',
                    100: 'rgb(245, 245, 245)',
                    200: 'rgb(234, 234, 234)',
                    300: 'rgb(219, 219, 219)',
                    400: 'rgb(175, 175, 175)',
                    500: 'rgb(130, 130, 130)',
                    600: 'rgb(97, 97, 97)',
                    700: 'rgb(69, 69, 69)',
                    800: 'rgb(42, 42, 42)',
                    900: 'rgb(28, 28, 28)'
                }
            },
            fontFamily: {
                poppins: ['Poppins', 'sans-serif'],
                inter: ['Inter', 'sans-serif'],
            },
            strokeWidth: {
                '0': '0',
                '4': '4',
                '10': '10',
            },
            aspectRatio: {
                43: "4 / 3"
            }
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
};
