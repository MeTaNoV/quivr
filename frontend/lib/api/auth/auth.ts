import { AxiosInstance } from "axios";

import { ApiKeyInfo } from "@/app/user/components/ApiKeyConfig/types";

// TODO(pg): finish this
export const createApiKey = async (
  axiosInstance: AxiosInstance
): Promise<ApiKeyInfo> => {
  const response = await axiosInstance.post<ApiKeyInfo>("/api-key");

  return response.data;
};

// TODO(pg): finish this
export const listApiKeys = async (axiosInstance: AxiosInstance): Promise<ApiKeyInfo[]> => {
  const response = await axiosInstance.get<ApiKeyInfo[]>("/api-key");

  return response.data;
}

// TODO(pg): finish this
export const deleteApiKey = async (axiosInstance: AxiosInstance) => {
  const response = await axiosInstance.delete("/api-key");

  return response.data;
}