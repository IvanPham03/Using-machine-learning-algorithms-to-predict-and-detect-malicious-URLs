import React from 'react';
import { Route, Outlet } from 'react-router-dom';

const createRoutes = (routes) => {
    return routes.map((route, index) => {
        const { path, component: Component, layout: Layout, children } = route;

        if (Layout) {
            // Route cha có layout, sử dụng Outlet cho các route con
            return (
                <Route
                    key={path || index}
                    path={path}
                    element={
                        <Layout>
                            {Component && <Component />}
                            <Outlet />
                        </Layout>
                    }
                >
                    {children && createRoutes(children)}
                </Route>
            );
        }

        // Route không có layout
        return <Route key={path || index} path={path} element={<Component />} />;
    });
};

export default createRoutes;
