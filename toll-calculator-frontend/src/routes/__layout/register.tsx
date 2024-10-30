import { Box, Button, Container, Flex, FormControl, FormErrorMessage, FormLabel, Input, Select, Text } from "@chakra-ui/react"
import { createFileRoute } from "@tanstack/react-router"
import { SubmitHandler, useForm } from "react-hook-form"
import { Vehicle } from "../../types/vehicle"
import { registrationPattern } from "../../utils"
import { useMutation } from "@tanstack/react-query"
import { registerTollEvent } from "../../api/tollService"

export const Route = createFileRoute("/__layout/register")({
    component: Register,
})

function Register() {
    return (
        <>
            <Container maxW="full">
                <Box pt={12} m={4}>
                    <Text fontSize="2xl">Register toll event</Text>
                    <RegisterEventForm />
                </Box>
            </Container>
        </>
    )
}

type RegisterTollEventForm = {
    registrationNumber: string
    vehicle: Vehicle
    date: string
    time: string
}

const RegisterEventForm = () => {
    const {
        register,
        handleSubmit,
        reset,
        formState: { errors, isSubmitting, isValid },
    } = useForm<RegisterTollEventForm>({
        mode: "onBlur",
        criteriaMode: "all",
        defaultValues: {
            registrationNumber: "",
            vehicle: Vehicle.Car,
            date: "2020-01-01",
            time: "00:00",
        },
    })

    const mutation = useMutation({
        mutationFn: (data: RegisterTollEventForm) =>
            registerTollEvent({
                "registration_number": data.registrationNumber,
                vehicle: data.vehicle,
                time: `${data.date} ${data.time}`,
            }),
        onSuccess: () => {
            reset()
        },
    })

    const onSubmit: SubmitHandler<RegisterTollEventForm> = (data) => {
        mutation.mutate(data)
    }

    return (
        <>
            <Flex mt={20} mb={10} direction={"row"} gap={10}>
                <FormControl isRequired isInvalid={!!errors.registrationNumber}>
                    <FormLabel htmlFor="registrationNumber">Registration number</FormLabel>
                    <Input
                        id="registrationNumber"
                        {...register("registrationNumber", {
                            required: "Email is required",
                            pattern: registrationPattern,
                        })}
                        placeholder="Registration number"
                    />
                    {errors.registrationNumber && <FormErrorMessage>{errors.registrationNumber.message}</FormErrorMessage>}
                </FormControl>
                <FormControl isRequired isInvalid={!!errors.vehicle}>
                    <FormLabel htmlFor="vehicle">Vehicle</FormLabel>
                    <Select
                        id="vehicle"
                        placeholder="Select vehicle"
                        {...register("vehicle", {
                            required: "Vehicle is required",
                        })}
                    >
                        <option value="car">Car</option>
                        <option value="motorbike">Motorbike</option>
                        <option value="tractor">Tractor</option>
                        <option value="emergency">Emergency</option>
                        <option value="diplomat">Diplomat</option>
                        <option value="foreign">Foreign</option>
                        <option value="military">Military</option>
                    </Select>
                    {errors.registrationNumber && <FormErrorMessage>{errors.registrationNumber.message}</FormErrorMessage>}
                </FormControl>
                <FormControl isRequired isInvalid={!!errors.date}>
                    <FormLabel htmlFor="date">Date</FormLabel>
                    <Input
                        id="date"
                        {...register("date", {
                            required: "Date is required",
                        })}
                        type="date"
                    />
                    {errors.date && <FormErrorMessage>{errors.date.message}</FormErrorMessage>}
                </FormControl>
                <FormControl isRequired isInvalid={!!errors.time}>
                    <FormLabel htmlFor="time">Time</FormLabel>
                    <Input
                        id="time"
                        {...register("time", {
                            required: "time is required",
                        })}
                        type="time"
                    />
                    {errors.time && <FormErrorMessage>{errors.time.message}</FormErrorMessage>}
                </FormControl>
            </Flex>
            <Button isDisabled={!isValid} colorScheme="blue" isLoading={isSubmitting} onClick={handleSubmit(onSubmit)}>
                Register
            </Button>
        </>
    )
}
