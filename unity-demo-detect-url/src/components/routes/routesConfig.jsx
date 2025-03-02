import { ClientLayout, NotFoundPage } from '../layouts'
import DemoDetectUrl from '../../pages/demo-detect-url'

const routesConfig = [
    {
        path: '/',
        layout: ClientLayout,
        children: [
            { path: '', component: DemoDetectUrl },
            { path: 'demo-detect-url', component: DemoDetectUrl },
        ],
    },
    {
        path: '*',
        component: NotFoundPage,
    },
];



export default routesConfig
