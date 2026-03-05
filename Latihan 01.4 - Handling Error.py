# Nama      : Raihan Naufal
# NIM       : 12550112671
# Kelas     : H
# Dosen     : Muhammad Affandes, S.T., M.T.


class Vehicle:
    def __init__(self, brand, model):
        if not isinstance(brand, str) or not isinstance(model, str):
            raise TypeError("Brand dan model harus berupa teks")

        self.brand = brand
        self.model = model

    def drive(self):
        print(f"\n{self.brand} {self.model} sedang berjalan.")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)

        if not isinstance(doors, int):
            raise TypeError("Jumlah pintu harus berupa angka")

        if doors <= 0:
            raise ValueError("Jumlah pintu harus lebih dari 0")

        self.doors = doors

    def honk(self):
        print("Klakson mobil: Beep! Beep!")


class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)

        if load_capacity <= 0:
            raise ValueError("Kapasitas muatan harus lebih dari 0")

        self.load_capacity = load_capacity

    def load(self, weight):
        try:
            if weight > self.load_capacity:
                raise ValueError("Muatan melebihi kapasitas truck")

            print(f"Truck berhasil memuat {weight} kg barang.")

        except ValueError as e:
            print("Error:", e)


# Program utama
def main():
    try:
        print("=== INPUT DATA MOBIL ===")
        brand_car = input("Masukkan merk mobil : ")
        model_car = input("Masukkan model mobil : ")
        doors = int(input("Masukkan jumlah pintu : "))

        my_car = Car(brand_car, model_car, doors)

        print("\n=== INPUT DATA TRUCK ===")
        brand_truck = input("Masukkan merk truck : ")
        model_truck = input("Masukkan model truck : ")
        capacity = int(input("Masukkan kapasitas muatan (kg) : "))

        my_truck = Truck(brand_truck, model_truck, capacity)

        print("\n=== OPERASI KENDARAAN ===")
        my_car.drive()
        my_car.honk()

        my_truck.drive()

        weight = int(input("Masukkan berat muatan truck (kg): "))
        my_truck.load(weight)

    except ValueError:
        print("Error: Input harus berupa angka pada bagian yang diminta.")

    except TypeError as e:
        print("Type Error:", e)

    except Exception as e:
        print("Terjadi kesalahan:", e)


if __name__ == "__main__":
    main()