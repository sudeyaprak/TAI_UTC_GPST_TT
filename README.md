# TAI_UTC_GPST_TT

## TAI (UTC)

1. Input:
The `TAI` function takes a single argument `UTC`, which is expected to be a list containing four elements: [Year, Month, Day, Second of day]. This represents a specific date and time in Coordinated Universal Time (UTC).

2. Purpose:
The primary purpose of the `TAI` function is to convert a given UTC date and time into the corresponding Julian Date in the International Atomic Time (TAI) system. The International Atomic Time (TAI) is a time scale based on a weighted average of the time kept by atomic clocks worldwide, and it serves as the basis for other time scales like UTC.

3. Calculation:
The function performs various mathematical operations to calculate the Julian Date, which is then converted into the TAI.

- Julian Date Calculation:
The function first calculates the Julian Date for the provided UTC date and time. This involves converting the calendar date (Year, Month, Day) into the Julian Day Number and then adding the fractional part of the day (represented by the `Second of day` value).

- UTC to Julian Date Conversion Formula:
The formula used to calculate the Julian Date is a modified version of the Julian Day Number formula, considering the fractional part of the day in hours (Second of day):

4. Return Value:
The function returns the calculated Julian Date (`julian_datetime`), which represents the given UTC date and time in the TAI system.

It's essential to note that the function's accuracy and applicability depend on the validity of the input UTC date and time, as well as the specific use case for which the conversion to TAI is intended.

Lastly, to ensure the accuracy and reliability of time-related calculations, it is recommended to use standard libraries or established time conversion methods provided by reputable sources, as they will be more up-to-date and account for any changes in timekeeping systems or leap seconds.

## GPST (UTC)

1. Input:
The `GPST` function takes a single argument `UTC`, which is expected to be a list containing four elements: [Year, Month, Day, Second of day]. This represents a specific date and time in Coordinated Universal Time (UTC).

2. Purpose:
The primary purpose of the `GPST` function is to convert a given UTC date and time into the corresponding Julian Date in the GPS Time (GPST) system. The GPS Time (GPST) is the time scale used by the Global Positioning System (GPS) satellites.

3. Calculation:
The function performs various mathematical operations to calculate the Julian Date, which then represents the GPS Time.

- Julian Date Calculation:
The function first calculates the Julian Date for the provided UTC date and time. This involves converting the calendar date (Year, Month, Day) into the Julian Day Number and then adding the fractional part of the day (represented by the `Second of day` value).

- UTC to Julian Date Conversion Formula:
The formula used to calculate the Julian Date is similar to the Julian Date formula used in previous examples, but with a slight modification to account for the time offset between UTC and GPST. In this case, the UTC time is adjusted by subtracting 9 seconds (UTC+9) to obtain the GPS Time.

4. Return Value:
The function returns the calculated Julian Date (`julian_datetime`), which represents the given UTC date and time converted to the GPS Time (GPST) system.

It's important to note that GPS Time (GPST) is different from UTC due to leap seconds adjustments and other factors. Therefore, it's crucial to use appropriate and up-to-date algorithms or libraries to perform accurate time conversions between different time scales, especially when dealing with critical applications like satellite navigation. The provided function may not handle leap seconds or other time adjustments, which are necessary for precise GPS-related calculations.

For critical and accurate GPS time conversions, it is recommended to use specialized libraries or APIs that provide the necessary functionalities and consider the complexities associated with timekeeping systems.

## TT (UTC)

1. Input:
The `TT` function takes a single argument `UTC`, which is expected to be a list containing four elements: [Year, Month, Day, Second of day]. This represents a specific date and time in Coordinated Universal Time (UTC).

2. Purpose:
The primary purpose of the `TT` function is to convert a given UTC date and time into the corresponding Julian Date in Terrestrial Time (TT). Terrestrial Time (TT) is a time scale that provides a continuous and uniform time scale independent of the Earth's rotation.

3. Calculation:
The function performs various mathematical operations to calculate the Julian Date, which then represents the Terrestrial Time (TT).

- Julian Date Calculation:
The function first calculates the Julian Date for the provided UTC date and time. This involves converting the calendar date (Year, Month, Day) into the Julian Day Number and then adding the fractional part of the day (represented by the `Second of day` value).

- UTC to Julian Date Conversion Formula:
The formula used to calculate the Julian Date is similar to the previous examples but with a slight modification to account for the time offset between UTC and TT. In this case, the UTC time is adjusted by adding 32,194 seconds (UTC+32,194) to obtain Terrestrial Time (TT).

4. Return Value:
The function returns the calculated Julian Date (`julian_datetime`), which represents the given UTC date and time converted to Terrestrial Time (TT) system.

As with previous functions, it's crucial to use appropriate and up-to-date algorithms or libraries for precise time conversions between different time scales, such as UTC and TT. The provided function does not account for factors like leap seconds or other time adjustments, which are necessary for accurate and reliable TT conversions.

For critical and accurate Terrestrial Time conversions, it is recommended to use specialized libraries or APIs that provide the necessary functionalities and consider the complexities associated with timekeeping systems.

