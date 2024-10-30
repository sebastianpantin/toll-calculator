import { Outlet, createRootRoute } from "@tanstack/react-router"
import React, { Suspense } from "react"

const loadDevtools = () =>
    Promise.all([import("@tanstack/router-devtools")]).then(([routerDevtools]) => {
        return {
            default: () => (
                <>
                    <routerDevtools.TanStackRouterDevtools />
                </>
            ),
        }
    })

const TanStackDevtools = process.env.NODE_ENV === "production" ? () => null : React.lazy(loadDevtools)

export const Route = createRootRoute({
    component: () => (
        <>
            <Outlet />
            <Suspense>
                <TanStackDevtools />
            </Suspense>
        </>
    ),
    notFoundComponent: () => <div>Not found</div>,
})
