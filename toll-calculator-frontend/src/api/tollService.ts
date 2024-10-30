import { Vehicle } from "../types/vehicle"
import { BACKEND_URL } from "./config"

export const registerTollEvent = async (data: { "registration_number": string; vehicle: Vehicle; time: string }) => {
    const res = await fetch(`${BACKEND_URL}/toll/register-toll-event`, {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ ...data }),
    })
    return res.json()
}
