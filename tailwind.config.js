module.exports = {
    content: [
        '*/templates/*/*.html',
        '*/templates/*.html'
    ],
    theme: {
        extend: {},
    },
    plugins: [],
	safelist: [
		'bg-green-100',
		'border-green-500',
		'text-green-800',
		'hover:text-green-600',
		'bg-red-100',
		'border-red-500',
		'text-red-800',
		'hover:text-red-600',
		'bg-yellow-100',
		'border-yellow-500',
		'text-yellow-800',
		'hover:text-yellow-600',
		'leading-normal', 'w-full', 'text-xs', 'italic', 'text-sm', 'border',
		'focus:outline-none', 'appearance-none', 'border-gray-300', 'px-4', 'text-gray-700',
		'rounded-lg', 'block', 'mb-2', 'font-bold', 'textinput', 'bg-white', 'text-gray-600',
		'py-2'
	]

}
